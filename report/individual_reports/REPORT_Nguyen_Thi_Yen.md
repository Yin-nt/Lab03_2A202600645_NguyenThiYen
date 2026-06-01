# Báo Cáo Cá Nhân: Lab 3 - Chatbot vs ReAct Agent

- **Họ tên sinh viên**: Nguyễn Thị Yến
- **Mã sinh viên**: 2A202600553 - Nhóm Lab03
- **Ngày**: 2026-06-01

---

## I. Đóng Góp Kỹ Thuật (15 điểm)

- **Công việc cá nhân phụ trách**: Thiết kế ReAct Agent.
- **Module liên quan**: `src/agent/agent.py`
- **Bằng chứng trong code**:
  - Class `ReActAgent` đã được định nghĩa với các thành phần chính: `llm`, `tools`, `max_steps`, và `history`.
  - Hàm `get_system_prompt()` đã mô tả danh sách tool được phép dùng và format làm việc theo `Thought`, `Action`, `Observation`, `Final Answer`.
  - Agent có giới hạn `max_steps` để tránh vòng lặp vô hạn.

Phần đóng góp tập trung vào thiết kế cấu trúc agent theo mô hình ReAct. Agent không trả lời trực tiếp như chatbot baseline mà được định hướng phải suy nghĩ từng bước, chọn tool phù hợp, nhận kết quả từ môi trường rồi mới đưa ra câu trả lời cuối. Thiết kế này là nền tảng để nối LLM với các function trong `src/tools/flight_tools.py`.

**Lưu ý kiểm tra thực tế**: Trong repo hiện tại, phần thiết kế agent đã có, nhưng vòng lặp thực thi trong `run()` vẫn còn TODO. Vì vậy đóng góp này được ghi nhận ở mức thiết kế/skeleton ReAct Agent, chưa phải agent hoàn chỉnh chạy production.

---

## II. Case Debugging (10 điểm)

- **Mô tả vấn đề**: Chatbot baseline trả lời trực tiếp cho câu hỏi chuyến bay mà không dùng tool, nên dễ đoán sai giá vé, chuyến bay rẻ nhất hoặc tổng tiền sau thuế.
- **Nguồn log**: `logs/2026-06-01.log`, các event `CHATBOT_CASE_START`, `LLM_METRIC`, `CHATBOT_CASE_END`.
- **Chẩn đoán**: Prompt baseline yêu cầu "Answer directly without using tools", nên model không có đường truy cập dữ liệu `FLIGHTS`. Với bài toán cần dữ liệu chính xác, thiết kế chatbot thường kém tin cậy hơn agent.
- **Cách khắc phục đề xuất**: Dùng `ReActAgent` để buộc model sinh `Action`, sau đó Python gọi tool thật và đưa kết quả về làm `Observation`.

---

## III. Nhận Xét Cá Nhân: Chatbot vs ReAct (10 điểm)

1. **Reasoning**: Khối `Thought` giúp agent tách phần suy luận khỏi hành động. Thay vì trả lời ngay, agent có thể xác định cần tìm chuyến bay, kiểm tra luật vé, tính giá rồi mới kết luận.
2. **Reliability**: Agent có thể tệ hơn chatbot nếu parser `Action` chưa ổn định hoặc vòng lặp chưa được cài đặt đầy đủ. Trong repo hiện tại, `run()` vẫn chưa chạy thật nên agent chưa thể vượt baseline về kết quả thực nghiệm.
3. **Observation**: `Observation` là điểm khác biệt quan trọng vì nó đưa dữ liệu thật từ tool quay lại cho LLM. Nhờ đó câu trả lời cuối có thể dựa trên kết quả function thay vì suy đoán.

---

## IV. Cải Tiến Tương Lai (5 điểm)

- **Scalability**: Tách agent thành các node riêng cho planning, tool execution và final response.
- **Safety**: Chỉ cho phép gọi tool trong whitelist, không dùng `eval()` với text do LLM sinh ra.
- **Performance**: Ghi thêm số vòng lặp, tool latency và số lỗi parse để đánh giá chất lượng agent theo từng lần chạy.

---

> [!NOTE]
> File này được tạo từ template cá nhân và đã ghi rõ phần công việc thật sự tồn tại trong repo.
