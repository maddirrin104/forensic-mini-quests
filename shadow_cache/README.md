# Shadow Cache

## 1. Nhận diện định dạng file

Bước đầu tiên là kiểm tra các chuỗi ký tự có thể đọc được trong file binary để dự đoán định dạng:

```bash
strings shadow_cache.bin | head -n 20
```

**Dấu hiệu nhận biết:**
Trong kết quả trả về, chuỗi `RDP8bmp` xuất hiện ngay ở đầu. Đây là Magic Byte đặc thù của file **Windows RDP Bitmap Cache** (phiên bản RDP 8.0 trở lên). Hệ thống này lưu trữ các mảnh hình ảnh của màn hình từ xa để tăng tốc độ hiển thị cho người dùng.

## 2. Công cụ

Sử dụng công cụ **bmc-tools**, một framework mã nguồn mở mạnh mẽ để phân tích và trích xuất dữ liệu từ các file cache của Windows RDP.

```bash
git clone https://github.com/ANSSI-FR/bmc-tools.git
```

## 3. Trích xuất các mảnh hình ảnh

Tiến hành trích xuất các tile hình ảnh riêng lẻ từ file `.bin` vào một thư mục đích:

```bash
mkdir output_images
python3 bmc-tools.py -s shadow_cache.bin -d ./output_images
```

**Kết quả:** Công cụ đã trích xuất thành công 650 file ảnh .bmp. Mỗi file là một mảnh nhỏ được lưu trữ trong bộ nhớ đệm.

## 4. Phân tích

Kiểm tra file ảnh tổng hợp để tìm kiếm các thông tin nhạy cảm.

### Kết quả quan sát:
Tại dải phía trên của bức ảnh tổng hợp, chúng ta tìm thấy flag được viết theo phong cách vẽ tay trên một nền trắng:

*   **Flag:** `FLAG{RDP_is_useful_yipeee}`

![flag](flag.png)