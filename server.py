"""
TravelBuddy Web Server — FastAPI backend with SSE streaming.
"""
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, StreamingResponse
from pydantic import BaseModel
from agent import graph
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
import uvicorn
import json
import asyncio

app = FastAPI(title="TravelBuddy API")

# --------------- Models ---------------
class ChatRequest(BaseModel):
    message: str
    history: list[dict] | None = None

# --------------- Streaming Endpoint ---------------
@app.post("/chat/stream")
async def chat_stream(req: ChatRequest):
    """Stream the agent response via Server-Sent Events."""

    async def event_generator():
        # Build message list
        messages = []
        if req.history:
            for msg in req.history:
                role = msg.get("role", "user")
                content = msg.get("content", "")
                if role == "user":
                    messages.append(HumanMessage(content=content))
                else:
                    messages.append(AIMessage(content=content))
        messages.append(HumanMessage(content=req.message))

        tool_calls_sent = set()

        try:
            async for event in graph.astream_events(
                {"messages": messages},
                version="v2"
            ):
                kind = event.get("event")

                # Stream tool call info
                if kind == "on_tool_start":
                    tool_name = event.get("name", "")
                    run_id = event.get("run_id", "")
                    if run_id not in tool_calls_sent:
                        tool_calls_sent.add(run_id)
                        data = json.dumps({"type": "tool_call", "name": tool_name})
                        yield f"data: {data}\n\n"

                # Stream LLM tokens (only from the final AI response, not tool-calling chunks)
                if kind == "on_chat_model_stream":
                    chunk = event.get("data", {}).get("chunk")
                    if chunk and hasattr(chunk, "content") and chunk.content:
                        # Only stream text content, skip tool call chunks
                        if not (hasattr(chunk, "tool_calls") and chunk.tool_calls):
                            data = json.dumps({"type": "token", "content": chunk.content})
                            yield f"data: {data}\n\n"

            # Signal done
            yield f"data: {json.dumps({'type': 'done'})}\n\n"

        except Exception as e:
            error_data = json.dumps({"type": "error", "content": str(e)})
            yield f"data: {error_data}\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        }
    )

# --------------- Non-streaming fallback ---------------
@app.post("/chat")
async def chat(req: ChatRequest):
    """Non-streaming fallback endpoint."""
    messages = []
    if req.history:
        for msg in req.history:
            role = msg.get("role", "user")
            content = msg.get("content", "")
            if role == "user":
                messages.append(("human", content))
            else:
                messages.append(("ai", content))
    messages.append(("human", req.message))

    result = graph.invoke({"messages": messages})
    tool_calls_info = []
    for msg in result["messages"]:
        if hasattr(msg, "tool_calls") and msg.tool_calls:
            for tc in msg.tool_calls:
                tool_calls_info.append({"name": tc["name"], "args": tc["args"]})

    return {"reply": result["messages"][-1].content, "tool_calls": tool_calls_info}

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return FileResponse("static/index.html")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
