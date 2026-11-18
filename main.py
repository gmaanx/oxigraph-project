import sys
import time
import pyoxigraph
from pyoxigraph import Store, NamedNode, Literal, Quad
import networkx as nx
import matplotlib

# Dùng backend Agg để vẽ và lưu file ảnh ổn định trên mọi hệ điều hành
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pyvis.network import Network

# Cấu hình hiển thị tiếng Việt có dấu trên cửa sổ dòng lệnh Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# Tiền tố đường dẫn dùng chung cho toàn bộ dữ liệu đồ thị của nhóm
BASE_URI = "http://ueh.edu.vn/qlmh/"


def rut_gon_ten(chuoi):
    """Cắt bỏ phần tiền tố BASE_URI để tên đỉnh và tên cạnh ngắn gọn hơn."""
    if chuoi.startswith(BASE_URI):
        return chuoi[len(BASE_URI):]
    return chuoi


def tv2_nap_du_lieu(store):
    """Nhiệm vụ TV2: Khởi tạo Store của Oxigraph và nạp bộ dữ liệu mẫu từ TV1."""
    print("\n" + "=" * 60)
    print("PHẦN TV2: KHỞI TẠO STORE VÀ NẠP DỮ LIỆU MẪU")
    print("=" * 60)

    # Nếu chưa có kho lưu trữ truyền vào thì khởi tạo một Store mới trong bộ nhớ
    if store is None:
        store = Store()

    # Hai dòng mẫu minh họa cách tạo đỉnh, giá trị chữ và thêm vào Store
    # Mẫu 1: Bộ ba nối từ đỉnh này sang đỉnh khác bằng NamedNode
    store.add(
        Quad(
            NamedNode(BASE_URI + "sv_an"),
            NamedNode(BASE_URI + "dang_ky_hoc"),
            NamedNode(BASE_URI + "mon_ltdt"),
        )
    )

    # Mẫu 2: Bộ ba nối từ đỉnh sang một chuỗi văn bản bằng Literal
    store.add(
        Quad(
            NamedNode(BASE_URI + "mon_ltdt"),
            NamedNode(BASE_URI + "ten_mon"),
            Literal("Lý thuyết đồ thị"),
        )
    )

    # ==========================================================
    # VÙNG CODE CỦA TV2:
    # Xem bảng dữ liệu trong file DATA_TV1.md mà TV1 đã chuẩn bị
    # rồi viết tiếp các lệnh store.add(Quad(...)) vào ngay bên dưới.
    # ==========================================================

    print(f"Đã nạp xong dữ liệu. Tổng số bộ ba hiện có trong Store: {len(store)}")
    return store


def tv3_truy_van_co_ban(store):
    """Nhiệm vụ TV3: Viết câu truy vấn SPARQL cơ bản dùng SELECT và WHERE."""
    print("\n" + "=" * 60)
    print("PHẦN TV3: TRUY VẤN SPARQL CƠ BẢN VỚI SELECT VÀ WHERE")
    print("=" * 60)

    # Câu truy vấn mẫu tìm mã môn và tên môn mà sinh viên sv_an đã đăng ký
    cau_truy_van = """
    PREFIX qlmh: <http://ueh.edu.vn/qlmh/>
    SELECT ?mon ?ten WHERE {
        qlmh:sv_an qlmh:dang_ky_hoc ?mon .
        ?mon qlmh:ten_mon ?ten .
    }
    """

    ket_qua = store.query(cau_truy_van)
    co_ket_qua = False
    print("Kết quả truy vấn mẫu các môn học của sv_an:")
    for dong in ket_qua:
        co_ket_qua = True
        ma_mon = rut_gon_ten(dong["mon"].value)
        ten_mon = dong["ten"].value
        print(f"  * Mã môn: {ma_mon} | Tên môn: {ten_mon}")

    if not co_ket_qua:
        print("  Chưa tìm thấy kết quả phù hợp.")

    # ==========================================================
    # VÙNG CODE CỦA TV3:
    # Viết thêm các câu truy vấn tìm đỉnh kế cận và lọc dữ liệu
    # với từ khóa FILTER hoặc OPTIONAL ngay bên dưới phần này.
    # ==========================================================


def tv4_truy_van_nang_cao(store):
    """Nhiệm vụ TV4: Kiểm tra liên thông với ASK và tìm chuỗi qua nhiều cạnh."""
    print("\n" + "=" * 60)
    print("PHẦN TV4: TRUY VẤN NÂNG CAO VỚI ASK VÀ CHUỖI LIÊN KẾT")
    print("=" * 60)

    # Phần 1: Dùng lệnh ASK kiểm tra nhanh xem có cạnh nối trực tiếp hay không
    cau_ask = """
    PREFIX qlmh: <http://ueh.edu.vn/qlmh/>
    ASK WHERE {
        qlmh:sv_an qlmh:dang_ky_hoc qlmh:mon_ltdt .
    }
    """
    co_lien_thong = bool(store.query(cau_ask))
    print(f"Kiểm tra sv_an có đăng ký môn mon_ltdt không: {co_lien_thong}")

    # Phần 2: Truy vấn chuỗi liên kết đi qua hai cạnh liên tiếp trong đồ thị
    cau_chuoi_canh = """
    PREFIX qlmh: <http://ueh.edu.vn/qlmh/>
    SELECT ?dinh_trung_gian ?dich WHERE {
        qlmh:sv_an qlmh:dang_ky_hoc ?dinh_trung_gian .
        ?dinh_trung_gian qlmh:ten_mon ?dich .
    }
    """
    ket_qua_chuoi = store.query(cau_chuoi_canh)
    print("Chuỗi liên kết từ sv_an qua đỉnh trung gian tới đích:")
    for dong in ket_qua_chuoi:
        trung_gian = rut_gon_ten(dong["dinh_trung_gian"].value)
        dich = rut_gon_ten(dong["dich"].value)
        print(f"  * sv_an => {trung_gian} => {dich}")

    # ==========================================================
    # VÙNG CODE CỦA TV4:
    # Sau khi TV2 nạp đủ bộ dữ liệu của TV1, viết thêm lệnh ASK
    # kiểm tra liên thông nhiều bậc và truy vấn đường đi dài hơn.
    # ==========================================================


def tv5_mo_rong_1_ve_do_thi(store):
    """Nhiệm vụ TV5 mở rộng 1: Chuyển dữ liệu Oxigraph sang NetworkX để vẽ trực quan."""
    print("\n" + "=" * 60)
    print("PHẦN TV5 MỞ RỘNG 1: VẼ ĐỒ THỊ CÓ HƯỚNG TỪ OXIGRAPH")
    print("=" * 60)

    do_thi = nx.DiGraph()

    # Duyệt toàn bộ bộ ba trong Store của Oxigraph để dựng các cạnh có hướng
    for bo_ba in store:
        chu_ngu = rut_gon_ten(bo_ba.subject.value)
        vi_ngu = rut_gon_ten(bo_ba.predicate.value)
        tan_ngu = rut_gon_ten(bo_ba.object.value)
        do_thi.add_edge(chu_ngu, tan_ngu, label=vi_ngu)

    if do_thi.number_of_nodes() == 0:
        print("Kho dữ liệu đang rỗng nên chưa thể vẽ đồ thị.")
        return

    # Vẽ đồ thị tĩnh ra file ảnh PNG bằng matplotlib
    fig, ax = plt.subplots(figsize=(10, 6))
    vi_tri = nx.spring_layout(do_thi, seed=42, k=1.5)
    nx.draw_networkx(
        do_thi,
        pos=vi_tri,
        ax=ax,
        with_labels=True,
        node_color="#AED6F1",
        node_size=2600,
        font_size=10,
        font_weight="bold",
        arrows=True,
        arrowsize=20,
        edge_color="#5D6D7E",
    )
    nhan_canh = nx.get_edge_attributes(do_thi, "label")
    nx.draw_networkx_edge_labels(
        do_thi,
        pos=vi_tri,
        edge_labels=nhan_canh,
        ax=ax,
        font_color="#B03A2E",
        font_size=9,
    )
    ax.set_title("Đồ thị quản lý môn học trong Oxigraph", fontsize=13)
    ax.axis("off")
    plt.tight_layout()
    ten_file_anh = "do_thi_mon_hoc.png"
    plt.savefig(ten_file_anh, dpi=150)
    plt.close(fig)

    # Xuất thêm đồ thị tương tác HTML bằng pyvis để kéo thả xem trực tiếp trên trình duyệt
    mang_html = Network(
        height="600px",
        width="100%",
        directed=True,
        bgcolor="#FFFFFF",
        font_color="#1B2631",
        cdn_resources="in_line",
    )
    for dinh in do_thi.nodes():
        mang_html.add_node(dinh, label=dinh, title=dinh)
    for dinh_dau, dinh_cuoi, du_lieu in do_thi.edges(data=True):
        nhan = du_lieu.get("label", "")
        mang_html.add_edge(dinh_dau, dinh_cuoi, label=nhan, title=nhan)
    ten_file_html = "do_thi_mon_hoc.html"
    mang_html.write_html(ten_file_html)

    print(f"Đã vẽ xong {do_thi.number_of_nodes()} đỉnh và {do_thi.number_of_edges()} cạnh.")
    print(f"Đã lưu ảnh đồ thị tại file: {ten_file_anh}")
    print(f"Đã lưu đồ thị tương tác tại file: {ten_file_html}")


def tv5_mo_rong_2_do_toc_do():
    """Nhiệm vụ TV5 mở rộng 2: Đo tốc độ nạp và truy vấn 5000 bộ ba giả lập."""
    print("\n" + "=" * 60)
    print("PHẦN TV5 MỞ RỘNG 2: ĐO TỐC ĐỘ NẠP VÀ TRUY VẤN 5000 BỘ BA")
    print("=" * 60)

    store_toc_do = Store()
    vi_ngu_dang_ky = NamedNode(BASE_URI + "dang_ky_hoc")

    # Bấm giờ quá trình tạo và nạp tự động 5000 bộ ba giả lập vào Store mới
    bat_dau_nap = time.perf_counter()
    for i in range(5000):
        sv_node = NamedNode(f"{BASE_URI}sv_gia_lap_{i}")
        mon_node = NamedNode(f"{BASE_URI}mon_gia_lap_{i % 50}")
        store_toc_do.add(Quad(sv_node, vi_ngu_dang_ky, mon_node))
    ket_thuc_nap = time.perf_counter()
    thoi_gian_nap_ms = (ket_thuc_nap - bat_dau_nap) * 1000

    # Bấm giờ chạy câu truy vấn SPARQL lọc danh sách sinh viên của một môn
    cau_truy_van_toc_do = """
    PREFIX qlmh: <http://ueh.edu.vn/qlmh/>
    SELECT ?sv WHERE {
        ?sv qlmh:dang_ky_hoc qlmh:mon_gia_lap_1 .
    }
    """
    bat_dau_truy_van = time.perf_counter()
    ket_qua_toc_do = list(store_toc_do.query(cau_truy_van_toc_do))
    ket_thuc_truy_van = time.perf_counter()
    thoi_gian_truy_van_ms = (ket_thuc_truy_van - bat_dau_truy_van) * 1000

    print(f"Tổng số bộ ba giả lập đã nạp: {len(store_toc_do)}")
    print(f"Thời gian nạp 5000 bộ ba: {thoi_gian_nap_ms:.2f} mili giây")
    print(f"Số kết quả tìm thấy khi truy vấn: {len(ket_qua_toc_do)}")
    print(f"Thời gian chạy truy vấn SPARQL: {thoi_gian_truy_van_ms:.2f} mili giây")


def tv5_mo_rong_3_duong_di_ngan_nhat(store):
    """Nhiệm vụ TV5 mở rộng 3: Tìm đường đi ngắn nhất giữa hai đỉnh bằng NetworkX."""
    print("\n" + "=" * 60)
    print("PHẦN TV5 MỞ RỘNG 3: TÌM ĐƯỜNG ĐI NGẮN NHẤT GIỮA HAI ĐỈNH")
    print("=" * 60)

    do_thi = nx.DiGraph()
    for bo_ba in store:
        chu_ngu = rut_gon_ten(bo_ba.subject.value)
        vi_ngu = rut_gon_ten(bo_ba.predicate.value)
        tan_ngu = rut_gon_ten(bo_ba.object.value)
        do_thi.add_edge(chu_ngu, tan_ngu, quan_he=vi_ngu)

    # Hai đỉnh mặc định chạy được ngay trên 2 dòng dữ liệu mẫu ban đầu
    # Khi đã có đủ dữ liệu của TV1, có thể đổi sang hai đỉnh bất kỳ để kiểm thử
    dinh_dau = "sv_an"
    dinh_cuoi = "Lý thuyết đồ thị"

    if dinh_dau not in do_thi or dinh_cuoi not in do_thi:
        print(f"Không tìm thấy đỉnh {dinh_dau} hoặc {dinh_cuoi} trong đồ thị.")
        return

    try:
        duong_di = nx.shortest_path(do_thi, source=dinh_dau, target=dinh_cuoi)
        so_buoc = len(duong_di) - 1
        print(f"Đường đi ngắn nhất từ {dinh_dau} đến {dinh_cuoi} gồm {so_buoc} bước:")
        print("  Thứ tự đỉnh: " + " => ".join(duong_di))
        for chi_so in range(so_buoc):
            u = duong_di[chi_so]
            v = duong_di[chi_so + 1]
            ten_canh = do_thi[u][v]["quan_he"]
            print(f"  Bước {chi_so + 1}: {u} ==[{ten_canh}]==> {v}")
    except nx.NetworkXNoPath:
        print(f"Không có đường đi có hướng từ {dinh_dau} đến {dinh_cuoi}.")


def main():
    """Hàm điều phối chạy tuần tự toàn bộ quy trình từ TV2 đến TV5."""
    print("KHỞI CHẠY CHƯƠNG TRÌNH ĐỒ ÁN OXIGRAPH QUẢN LÝ MÔN HỌC")
    store = Store()
    store = tv2_nap_du_lieu(store)
    tv3_truy_van_co_ban(store)
    tv4_truy_van_nang_cao(store)
    tv5_mo_rong_1_ve_do_thi(store)
    tv5_mo_rong_2_do_toc_do()
    tv5_mo_rong_3_duong_di_ngan_nhat(store)
    print("\nHoàn tất toàn bộ chương trình.")


if __name__ == "__main__":
    main()
