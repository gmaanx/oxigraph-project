# Đồ án Oxigraph Quản lý môn học bằng Python

Bộ khung mã nguồn Python và tài liệu nhóm cho đồ án môn Lý thuyết đồ thị, tìm hiểu hệ quản trị cơ sở dữ liệu đồ thị Oxigraph thông qua thư viện `pyoxigraph`.

## 1. Cấu trúc thư mục

```text
oxigraph/
├── main.py              # File code chính chia sẵn hàm từ TV2 đến TV5
├── DATA_TV1.md          # Bảng dữ liệu mẫu 10 đến 15 đỉnh của TV1
├── BAO_CAO_CHUNG.md     # Khung báo cáo chia sẵn từ Phần 1 đến Phần 5
├── TOM_TAT_ON_BAI.md    # Tóm tắt ngắn gọn luồng chạy để ôn thi vấn đáp
├── requirements.txt     # Danh sách các thư viện cần cài đặt
├── .gitignore           # Danh sách thư mục và file Git tự động bỏ qua
└── README.md            # Tài liệu hướng dẫn quy trình làm việc nhóm qua Git
```

## 2. Phân công nhiệm vụ và thứ tự ghép nối

Tất cả thành viên cùng làm việc theo luồng truyền dữ liệu tuần tự từ TV1 đến TV5. Không tự ý đổi tên các hàm trong `main.py` để tránh gãy luồng gọi hàm khi gộp code.

| Thành viên | Nhánh gợi ý | File và hàm phụ trách | Giai đoạn |
| :--- | :--- | :--- | :--- |
| **TV1** | `tv1` | File `DATA_TV1.md`, `BAO_CAO_CHUNG.md` Phần 1, `TOM_TAT_ON_BAI.md` Mục TV1 | Giai đoạn 1 |
| **TV2** | `tv2` | Hàm `tv2_nap_du_lieu` trong `main.py`, Phần 2 báo cáo và tóm tắt TV2 | Giai đoạn 2 |
| **TV3** | `tv3` | Hàm `tv3_truy_van_co_ban` trong `main.py`, Phần 3 báo cáo và tóm tắt TV3 | Giai đoạn 3 |
| **TV4** | `tv4` | Hàm `tv4_truy_van_nang_cao` trong `main.py`, Phần 4 báo cáo và tóm tắt TV4 | Giai đoạn 3 |
| **TV5** | `tv5` | Khung dự án ban đầu, 3 hàm `tv5_mo_rong_*` trong `main.py`, Phần 5 báo cáo | Khởi tạo và tổng hợp |

Lưu ý quan trọng khi sửa code:
1. Chỉ sửa đúng vùng code và mục tài liệu được giao cho mình, không sửa nhầm sang hàm của bạn khác.
2. Sau khi sửa xong nhớ chạy thử `python main.py` để chắc chắn chương trình vẫn chạy hết từ đầu đến cuối không báo lỗi.

## 3. Lần đầu tham gia: Clone dự án và cài môi trường

Lệnh `git clone` **chỉ thực hiện đúng một lần duy nhất** lúc mới bắt đầu tải dự án về máy. Những ngày sau hoặc khi chờ tới lượt nhiệm vụ của mình, bạn **không cần xóa thư mục đi để clone lại**.

### Bước 1: Chấp nhận lời mời cộng tác trên GitHub

Trước khi thao tác, mở email hoặc truy cập https://github.com/gmaanx/oxigraph-project/invitations và bấm **Accept invitation** để tài khoản của bạn có quyền đẩy nhánh lên kho mã nguồn chung.

### Bước 2: Tải dự án về máy tính

Mở Terminal hoặc PowerShell tại thư mục muốn lưu bài rồi chạy:

```bash
git clone https://github.com/gmaanx/oxigraph-project.git
cd oxigraph-project
```

Mặc định sau khi `git clone`, máy bạn sẽ tải về nhánh gốc `main`. Nếu muốn tải thêm một nhánh cụ thể của thành viên khác đã có trên GitHub về máy để xem hoặc chạy thử, dùng lệnh:

```bash
git fetch origin
git switch ten_nhanh
```

### Bước 3: Tạo môi trường ảo và cài thư viện

File `.gitignore` đã tự động bỏ qua cả `.venv` lẫn `venv`, nên thư mục môi trường ảo sẽ không bị đẩy nhầm lên GitHub. Thư viện `pyoxigraph` hoạt động ổn định từ Python 3.10 trở lên, vì vậy nếu máy cài nhiều phiên bản Python hãy ưu tiên dùng Python 3.12 hoặc 3.13.

Trên Windows PowerShell:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Nếu PowerShell báo lỗi chính sách không cho chạy script kích hoạt, có thể gọi thẳng file trong `.venv` mà không cần kích hoạt:

```powershell
.\.venv\Scripts\pip.exe install -r requirements.txt
.\.venv\Scripts\python.exe main.py
```

Trên Windows CMD:

```cmd
py -3.12 -m venv .venv
.venv\Scripts\activate.bat
pip install -r requirements.txt
```

Trên macOS hoặc Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Sau khi cài xong thư viện, chạy thử chương trình khung ngay bằng lệnh:

```bash
python main.py
```

## 4. Khi tới lượt nhiệm vụ của bạn: Có cần clone lại không?

Câu trả lời là **KHÔNG cần clone lại**. Khi thành viên giai đoạn trước đã gộp code xong vào `main` và báo tới lượt bạn làm, bạn chỉ cần mở lại thư mục `oxigraph-project` đã có sẵn trên máy và làm theo một trong hai trường hợp dưới đây:

### Trường hợp 1: Bạn bắt đầu nhiệm vụ lần đầu và chưa tạo nhánh cá nhân

Chuyển về nhánh `main`, kéo toàn bộ code mới nhất mà các bạn giai đoạn trước vừa hoàn thành về máy, sau đó mới tách nhánh riêng cho mình:

```text
                                       o===o===o  nhánh tv2 dùng git switch -c tv2
                                      /
o=========o=========o================o===> nhánh main sau khi git pull origin main
  TV1 đã hoàn thành và gộp vào main
```

Lệnh thực hiện cho ví dụ TV2:

```bash
git switch main
git pull origin main
git switch -c tv2
```

Thay `tv2` bằng tên nhánh của bạn theo bảng phân công ở Mục 2. Nhờ tạo nhánh sau khi `git pull origin main`, nhánh cá nhân của bạn sẽ có sẵn đầy đủ dữ liệu và code của các bạn làm trước.

### Trường hợp 2: Bạn đã tạo nhánh cá nhân từ trước

Nếu bạn đã lỡ tạo nhánh cá nhân từ mấy hôm trước khi `main` chưa có code mới, hãy cập nhật code mới nhất từ `main` đắp sang nhánh của bạn:

```text
o=========o====================o===> nhánh main dùng git pull origin main
           \                    \
            o======o=============o===o===> nhánh tv3 dùng git merge main rồi code tiếp
             code cũ của TV3
```

Lệnh thực hiện:

```bash
git switch main
git pull origin main
git switch tv3
git merge main
```

## 5. Hướng dẫn trực quan cách phân nhánh và chuyển nhánh

Tuyệt đối không viết code trực tiếp khi đang đứng ở nhánh `main`. Sơ đồ luồng phân nhánh và gộp nhánh của cả nhóm như sau:

```text
                TV1 soạn bảng dữ liệu              TV3 viết truy vấn cơ bản
               o===o===o  nhánh tv1               o===o===o  nhánh tv3
              /         \                        /         \
o============o===========o============o=========o===========o===> nhánh main chuẩn
              \                      /
               o=======o=======o====o  nhánh tv2 gộp vào main
                TV2 nạp dữ liệu vào Store
```

### Tạo nhánh mới bằng cờ `-c` hoặc `-b`

Sau khi đã đứng ở bản `main` mới nhất, dùng một trong hai lệnh tương đương dưới đây để vừa tạo nhánh mới vừa chuyển sang nhánh đó. Ví dụ cho TV2:

```bash
# Cách 1 dùng lệnh git switch kèm cờ -c viết tắt của create
git switch -c tv2

# Cách 2 dùng lệnh git checkout kèm cờ -b viết tắt của branch
git checkout -b tv2
```

### Kiểm tra nhánh hiện tại trước khi gõ code

Luôn chạy lệnh dưới đây trước khi sửa file:

```bash
git branch
```

Màn hình sẽ hiện danh sách nhánh trên máy bạn như sau:

```text
  main
* tv2
```

Phải chắc chắn dấu sao `*` đang nằm trước tên nhánh cá nhân của bạn như `* tv2` chứ không nằm trước `main`.

### Chuyển qua lại giữa các nhánh đã tạo sẵn

Cờ `-c` và `-b` chỉ dùng duy nhất một lần lúc khởi tạo nhánh mới. Những ngày làm việc tiếp theo, khi nhánh đã có sẵn trên máy, chỉ gõ tên nhánh mà không thêm `-c` hay `-b`:

```bash
git switch tv2
# Hoặc
git checkout tv2
```

Lưu ý trước khi chuyển sang nhánh khác, bạn nhớ lưu và `git commit` những gì đang sửa dở ở nhánh hiện tại.

## 6. Lưu code, đẩy nhánh lên GitHub và gửi yêu cầu gộp code

Sau khi viết xong code trên nhánh cá nhân và chạy thử ổn định bằng `python main.py`, thực hiện lần lượt các bước sau để gửi yêu cầu gộp code vào `main`:

### Bước 1: Kiểm tra lại các file đã sửa

```bash
git status
git diff
```

Đảm bảo chỉ có đúng những file thuộc nhiệm vụ của bạn bị thay đổi, không sửa nhầm sang phần của thành viên khác.

### Bước 2: Đóng gói thay đổi bằng git add và git commit

Chỉ `git add` đúng tên file bạn phụ trách để không đẩy nhầm các file nháp chạy thử:

```bash
git add main.py BAO_CAO_CHUNG.md TOM_TAT_ON_BAI.md
git commit -m "TV2 hoan thanh ham nap du lieu"
```

### Bước 3: Đồng bộ với main lần cuối và đẩy nhánh lên GitHub

```bash
git fetch origin
git merge origin/main
git push -u origin tv2
```

Thay `tv2` bằng tên nhánh của bạn. Từ lần đẩy thứ hai trở đi trên cùng nhánh đó, chỉ cần gõ ngắn gọn `git push` là đủ.

### Bước 4: Tạo yêu cầu gộp code Pull Request trên GitHub

Trên GitHub, thao tác xin gộp nhánh của bạn vào `main` được gọi là tạo **Pull Request**. Thực hiện chi tiết như sau:

1. Mở trình duyệt truy cập https://github.com/gmaanx/oxigraph-project.
2. **Cách nhanh ngay sau khi vừa push**: Ở đầu trang sẽ xuất hiện khung màu vàng hiện tên nhánh bạn vừa đẩy lên, bấm ngay nút màu xanh **Compare & pull request**.
3. **Cách làm nếu không thấy khung màu vàng**:
   * Bấm vào thẻ **Pull requests** trên thanh menu ngang hoặc vào thẳng https://github.com/gmaanx/oxigraph-project/pulls.
   * Bấm nút màu xanh **New pull request** ở góc phải.
   * Nhìn hai ô chọn nhánh, giữ nguyên ô bên trái **base** là **`main`** và bấm chọn ô bên phải **compare** là nhánh của bạn như **`tv2`**.
   * Kéo xuống dưới xem lại phần code thay đổi rồi bấm nút xanh **Create pull request**.
4. Tại trang điền thông tin:
   * Ô tiêu đề ghi rõ mã thành viên và nội dung đã làm, ví dụ `TV2 hoan thanh ham nap du lieu`.
   * Ô mô tả bên dưới ghi ngắn gọn kết quả chạy thử nếu cần.
   * Bấm nút xanh **Create pull request** để hoàn tất gửi yêu cầu gộp code, sau đó nhắn lên nhóm chat để nhóm trưởng kiểm tra.

Mẹo quan trọng: Nếu sau khi đã gửi Pull Request mà nhóm trưởng góp ý cần sửa lại vài dòng code, bạn **không cần đóng hay tạo lại Pull Request mới**. Bạn chỉ việc mở lại nhánh cá nhân dưới máy, sửa code, chạy lại `git add`, `git commit` và `git push` thì trang Pull Request cũ trên GitHub sẽ tự động cập nhật theo code mới nhất của bạn.

## 7. Hướng dẫn duyệt và gộp code Merge vào nhánh main

Nhóm trưởng kiểm tra kỹ thay đổi trước khi bấm gộp để tránh đè mất code ở các file dùng chung như `main.py` hoặc `BAO_CAO_CHUNG.md`.

### Cách 1: Duyệt và gộp trực tiếp trên web GitHub

1. Mở danh sách yêu cầu tại https://github.com/gmaanx/oxigraph-project/pulls và bấm vào Pull Request của thành viên.
2. Mở thẻ **Files changed** để rà soát các dòng thêm mới màu xanh và dòng xóa đi màu đỏ, đảm bảo không xóa nhầm hàm của thành viên khác.
3. Quay lại thẻ **Conversation**:
   * Nếu hiện thông báo xanh **This branch has no conflicts with the base branch** thì bấm **Merge pull request** rồi bấm **Confirm merge**.
   * Nếu hiện cảnh báo xung đột thì bấm nút **Resolve conflicts** ngay trên web, giữ lại phần code đúng của cả hai thành viên, xóa các dòng đánh dấu xung đột, sau đó bấm **Mark as resolved** rồi **Commit merge** và tiến hành **Merge pull request**.

### Cách 2: Gộp bằng dòng lệnh trên máy tính

Nếu muốn kéo nhánh của thành viên về chạy thử trên máy trước khi gộp vào `main`, dùng chuỗi lệnh sau:

```bash
git fetch origin
git switch main
git pull origin main
git merge origin/tv2
git push origin main
```

## 8. Một số lệnh cứu nguy thường gặp

1. Lỡ tay sửa nhầm file khi chưa commit và muốn khôi phục file đó về nguyên trạng ban đầu:
   ```bash
   git restore ten_file.py
   ```
2. Muốn kiểm tra xem lịch sử các lần lưu commit trên nhánh hiện tại đã có những gì:
   ```bash
   git log --oneline -n 5
   ```
3. Muốn bỏ qua các thay đổi chưa kịp lưu để kéo mới hoàn toàn từ `main`:
   ```bash
   git switch main
   git pull origin main
   ```
