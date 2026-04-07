# Hướng dẫn chạy giao diện TravelBuddy

Đây là phần giao diện người dùng (UI) cho trợ lý du lịch AI TravelBuddy. Làm theo các bước dưới đây để khởi chạy ứng dụng web trên máy của bạn.

## 🚀 Cách khởi chạy

**1. Cài đặt các thư viện cần thiết (nếu chưa cài):**
```bash
pip install fastapi uvicorn pydantic langchain-core langgraph langchain_openai
```

**2. Cấu hình biến môi trường:**
Đảm bảo bạn đã có file `.env` ở thư mục gốc (cùng cấp với `server.py`) và chứa API key hợp lệ:
```env
OPENAI_API_KEY=your_api_key_here
```

**3. Khởi chạy Server:**
Từ thư mục gốc chứa file `server.py`, hãy chạy lệnh:
```bash
python server.py
```
*(Server sẽ bắt đầu chạy nhờ uvicorn)*

**4. Mở giao diện trên trình duyệt:**
Mở trình duyệt web của bạn và truy cập vào đường dẫn:
👉 **[http://localhost:8000](http://localhost:8000)**


---

## 📸 Hình ảnh giao diện

![giao diện](Giao%20diện.png)
