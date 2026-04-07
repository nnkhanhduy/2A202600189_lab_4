# BÁO CÁO KẾT QUẢ TEST CASES - TRAVELBUDDY

### Test 1 — Direct Answer (Không cần tool)
```text
Bạn: Xin chào! Tôi đang muốn đi du lịch nhưng chưa biết đi đâu

TravelBuddy đang suy nghĩ...
Trả lời trực tiếp

TravelBuddy: Chào bạn! Thật tuyệt khi bạn muốn đi du lịch! Có nhiều địa điểm thú vị tại Việt Nam mà bạn có thể khám phá. Bạn thích biển, núi, hay thành phố năng động? Hoặc nếu bạn có một ngân sách cụ thể hoặc khoảng thời gian đi du lịch, hãy cho mình biết để mình có thể tư vấn tốt hơn nhé!
```

### Test 2 — Single Tool Call
```text
Bạn: Tìm giúp tôi chuyến bay từ Hà Nội đi Đà Nẵng

TravelBuddy đang suy nghĩ...
Gọi tool: search_flights({'origin': 'Hà Nội', 'destination': 'Đà Nẵng'})
Trả lời trực tiếp

TravelBuddy: Đây là các chuyến bay từ Hà Nội đến Đà Nẵng mà tôi tìm thấy:    

1. **Vietnam Airlines** | 06:00→07:20 | Economy | **1.450.000đ**
2. **Vietnam Airlines** | 14:00→15:20 | Business | **2.800.000đ**
3. **VietJet Air** | 08:30→09:50 | Economy | **890.000đ**
4. **Bamboo Airways** | 11:00→12:20 | Economy | **1.200.000đ**

Nếu bạn cần thêm thông tin về khách sạn hay ngân sách, hãy cho tôi biết nhé! 
```

### Test 3 — Multi-Step Tool Chaining
```text
Bạn: Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, budget 5 triệu. Tư vấn giúp!

TravelBuddy đang suy nghĩ...
Gọi tool: search_flights({'origin': 'Hà Nội', 'destination': 'Phú Quốc'})
Gọi tool: search_hotels({'city': 'Phú Quốc', 'max_price_per_night': 2500000})
Gọi tool: calculate_budget({'total_budget': 5000000, 'expenses': 'vé_máy_bay:1100000,khách_sạn:1600000'})
Trả lời trực tiếp

TravelBuddy: Dưới đây là những thông tin tư vấn cho chuyến đi từ Hà Nội đến Phú Quốc của bạn:

### Chuyến bay:
1. **VietJet Air | 16:00→18:15 | economy | 1.100.000đ** (chuyến rẻ nhất)

### Khách sạn:
1. **Lahana Resort** | 3 sao | 800.000đ/đêm | Khu vực: Dương Đông | Rating: 4.0 (2 đêm: 1.600.000đ)
   
### Tổng chi phí ước tính:
- Vé máy bay: 1.100.000đ
- Khách sạn: 1.600.000đ
- **Tổng cộng: 2.700.000đ**

#### Gợi ý thêm:
- Ngân sách của bạn là 5.000.000đ, sau khi trừ đi tổng chi phí, bạn vẫn còn 2.300.000đ. Bạn có thể sử dụng khoản ngân sách còn lại cho việc ăn uống, tham quan hoặc mua sắm tại Phú Quốc.

Nếu bạn cần thêm thông tin hay hỗ trợ gì khác, đừng ngần ngại hỏi nhé!
```

### Test 4 — Missing Info / Clarification
```text
Bạn: Tôi muốn đặt khách sạn

TravelBuddy đang suy nghĩ...
Trả lời trực tiếp

TravelBuddy: Bạn định đặt khách sạn ở thành phố nào và ngân sách mỗi đêm là bao nhiêu?
```

### Test 5 — Guardrail / Refusal
```text
Bạn: Giải giúp tôi bài tập lập trình Python về linked list

TravelBuddy đang suy nghĩ...
Trả lời trực tiếp

TravelBuddy: Xin lỗi, nhưng mình chỉ có thể hỗ trợ về du lịch và đặt vé, không thể giúp bạn với bài tập lập trình. Nếu bạn cần thông tin về chuyến đi, khách sạn hay các điểm đến, hãy cho mình biết nhé!
```
