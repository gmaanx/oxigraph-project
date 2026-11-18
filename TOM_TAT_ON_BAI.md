# Tóm tắt ôn bài thuyết trình cho cả nhóm

Tài liệu này giúp cả 5 thành viên hiểu nhanh luồng chạy từ đầu đến cuối của đồ án, sẵn sàng trả lời và thuyết trình khi giảng viên gọi ngẫu nhiên bất kỳ ai trong nhóm.

## Bức tranh tổng thể luồng dữ liệu

Dữ liệu đi theo một đường thẳng xuyên suốt 5 thành viên:

1. TV1 thiết kế bảng các bộ ba Chủ ngữ, Vị ngữ, Tân ngữ về chủ đề Quản lý môn học.
2. TV2 chuyển từng dòng trong bảng của TV1 thành đối tượng `Quad` chứa `NamedNode` và `Literal`, rồi nạp vào kho `Store` của Oxigraph và trả về `store`.
3. TV3 nhận `store` từ TV2, chạy truy vấn SPARQL `SELECT` với `WHERE` để lấy thông tin chi tiết và tìm các đỉnh kế cận.
4. TV4 nhận `store` từ TV2, chạy truy vấn `ASK` để kiểm tra có liên thông giữa hai đỉnh hay không và tìm đường đi qua nhiều cạnh nối tiếp nhau.
5. TV5 nhận `store` để vẽ đồ thị có hướng ra ảnh và file HTML, tìm đường đi ngắn nhất giữa hai đỉnh, đồng thời chạy thêm hàm đo tốc độ nạp và truy vấn 5000 bộ ba giả lập.

---

## Phần tóm tắt riêng của từng thành viên

Mỗi thành viên sau khi viết xong code của mình hãy tự điền lại 3 đến 5 dòng thật ngắn gọn giải thích phần việc mình đã làm vào đúng mục bên dưới.

### Mục TV1: Lý thuyết RDF và bảng dữ liệu mẫu

* Ý 1: ... tự điền sau khi làm xong `DATA_TV1.md` ...
* Ý 2: ...
* Ý 3: ...

### Mục TV2: Nạp dữ liệu vào Oxigraph Store

* Ý 1: ... tự điền sau khi hoàn thành `tv2_nap_du_lieu` ...
* Ý 2: ...
* Ý 3: ...

### Mục TV3: Truy vấn SPARQL cơ bản SELECT và WHERE

* Ý 1: ... tự điền sau khi hoàn thành `tv3_truy_van_co_ban` ...
* Ý 2: ...
* Ý 3: ...

### Mục TV4: Truy vấn nâng cao ASK và chuỗi nhiều cạnh

* Ý 1: ... tự điền sau khi hoàn thành `tv4_truy_van_nang_cao` ...
* Ý 2: ...
* Ý 3: ...

### Mục TV5: Dựng khung Git và 3 phần mở rộng

* Mở đầu dự án: Em dựng sẵn cấu trúc file `main.py` theo từng hàm nối tiếp nhau và hướng dẫn Git trong `README.md` để 4 bạn còn lại code mà không đè lên nhau.
* Mở rộng 1: Hàm `tv5_mo_rong_1_ve_do_thi` quét từng bộ ba trong `Store` đưa sang `nx.DiGraph` rồi vẽ ra file ảnh `do_thi_mon_hoc.png` và trang web kéo thả `do_thi_mon_hoc.html`.
* Mở rộng 2: Hàm `tv5_mo_rong_2_do_toc_do` tự sinh 5000 bộ ba giả lập vào một `Store` riêng và dùng `time.perf_counter` bấm giờ nạp cùng giờ truy vấn SPARQL tính bằng mili giây.
* Mở rộng 3: Hàm `tv5_mo_rong_3_duong_di_ngan_nhat` lấy các cạnh từ Oxigraph sang `nx.DiGraph` rồi gọi `nx.shortest_path` để in ra đường đi ít bước nhất giữa hai đỉnh.
