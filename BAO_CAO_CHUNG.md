# Báo cáo chung đồ án môn Lý thuyết đồ thị

Đề tài: Tìm hiểu hệ quản trị cơ sở dữ liệu đồ thị Oxigraph qua thư viện `pyoxigraph` trên Python với bài toán Quản lý môn học tại trường đại học.

## Thông tin phân công nhóm 5 thành viên

| Thành viên | Vai trò chính | Nhánh Git | Trạng thái |
| :--- | :--- | :--- | :--- |
| TV1 | Cơ sở lý thuyết RDF, vẽ sơ đồ và lập bảng dữ liệu 10 đến 15 đỉnh | `tv1` | Chưa hoàn thành |
| TV2 | Cài đặt `pyoxigraph` và nạp bộ dữ liệu mẫu vào `Store` | `tv2` | Chưa hoàn thành |
| TV3 | Lý thuyết SPARQL và viết hàm truy vấn cơ bản `SELECT` với `WHERE` | `tv3` | Chưa hoàn thành |
| TV4 | Viết hàm truy vấn nâng cao `ASK` và đường đi nhiều cạnh | `tv4` | Chưa hoàn thành |
| TV5 | Khởi tạo khung Git và viết 3 phần mở rộng trực quan, đo tốc độ, đường đi ngắn nhất | `tv5` | Đã dựng khung |

---

## Phần 1: Cơ sở lý thuyết mô hình RDF và bộ dữ liệu mẫu

Phụ trách: Thành viên 1.

Gợi ý nội dung cần viết:
* Trình bày tổng quan phần mềm Oxigraph là hệ quản trị cơ sở dữ liệu đồ thị hỗ trợ mô hình dữ liệu RDF.
* Giải thích cách đồ thị có hướng được biểu diễn bằng từng bộ ba gồm Chủ ngữ đóng vai trò đỉnh bắt đầu, Vị ngữ là cạnh có hướng thể hiện mối quan hệ và Tân ngữ là đỉnh kết thúc hoặc giá trị chữ số.
* Đưa sơ đồ đồ thị mẫu gồm 10 đến 15 đỉnh chủ đề Quản lý môn học tại trường đại học và bảng các bộ ba từ file [DATA_TV1.md](DATA_TV1.md) vào phần này.

... Thành viên 1 điền nội dung báo cáo Phần 1 tại đây ...

---

## Phần 2: Cài đặt môi trường và nạp dữ liệu vào Oxigraph Store

Phụ trách: Thành viên 2.

Gợi ý nội dung cần viết:
* Trình bày các bước cài đặt Python, tạo môi trường ảo `.venv` và cài đặt thư viện `pyoxigraph`.
* Giải thích ý nghĩa các thành phần đã sử dụng trong hàm `tv2_nap_du_lieu` gồm `Store`, `NamedNode`, `Literal`, `Quad` và lệnh `store.add`.
* Chụp ảnh màn hình kết quả chạy thử chứng minh toàn bộ bộ ba của TV1 đã nạp thành công vào kho dữ liệu.

... Thành viên 2 điền nội dung báo cáo Phần 2 tại đây ...

---

## Phần 3: Ngôn ngữ truy vấn SPARQL và truy vấn cơ bản

Phụ trách: Thành viên 3.

Gợi ý nội dung cần viết:
* Trình bày cách ngôn ngữ truy vấn SPARQL hoạt động dựa trên việc khớp mẫu bộ ba trong đồ thị có hướng.
* Giải thích cú pháp câu truy vấn `SELECT` và `WHERE`, cách khai báo biến bắt đầu bằng dấu hỏi chấm, cách tìm các đỉnh kế cận và cách dùng `FILTER` để lọc dữ liệu.
* Đính kèm các câu truy vấn đã viết trong hàm `tv3_truy_van_co_ban` cùng kết quả thực tế in trên màn hình.

... Thành viên 3 điền nội dung báo cáo Phần 3 tại đây ...

---

## Phần 4: Truy vấn nâng cao với ASK và đường đi qua nhiều đỉnh

Phụ trách: Thành viên 4.

Gợi ý nội dung cần viết:
* Giải thích công dụng của lệnh `ASK` trong SPARQL dùng để trả lời đúng hoặc sai khi kiểm tra tính liên thông giữa hai đỉnh.
* Trình bày cách ghép nhiều mẫu cạnh liên tiếp trong khối `WHERE` để lần theo đường đi qua nhiều đỉnh trung gian.
* Ghi lại kết quả kiểm tra liên thông và đường đi tìm được từ hàm `tv4_truy_van_nang_cao`.

... Thành viên 4 điền nội dung báo cáo Phần 4 tại đây ...

---

## Phần 5: Quy trình làm việc nhóm qua Git và 3 phần mở rộng

Phụ trách: Thành viên 5.

Gợi ý nội dung cần viết:
* Mô tả quy trình chuẩn hóa khung dự án ban đầu, phân nhánh `tv1` đến `tv5` và gộp code lần lượt về `main`.
* Trình bày phần mở rộng 1: Trích xuất toàn bộ bộ ba từ `Store` của Oxigraph sang đồ thị có hướng `nx.DiGraph` của thư viện `networkx`, xuất ảnh `do_thi_mon_hoc.png` bằng `matplotlib` và file web tương tác `do_thi_mon_hoc.html` bằng `pyvis`.
* Trình bày phần mở rộng 2: Dùng thư viện `time` tạo tự động 5000 bộ ba giả lập, đo tốc độ nạp vào `Store` và tốc độ chạy truy vấn SPARQL theo đơn vị mili giây.
* Trình bày phần mở rộng 3: Dùng thuật toán tìm đường đi ngắn nhất `nx.shortest_path` giữa hai đỉnh bất kỳ trên đồ thị trích xuất từ Oxigraph.

... Thành viên 5 cập nhật số liệu thực tế và hình ảnh sau khi ghép đủ code của nhóm ...
