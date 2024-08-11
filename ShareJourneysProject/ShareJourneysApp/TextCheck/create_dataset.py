import pandas as pd

# Dữ liệu mẫu với văn bản tiếng Anh và tiếng Việt và nhãn
data = {
    'text': [
        "This is a normal content.",
        "This content contains sensitive information.",
        "Here is some regular text.",
        "Sensitive data detected in this text.",
        "Just another normal content.",
        "This article includes some sensitive details.",
        "F**k this! This is sh*t!",
        "Đ*o tin được, thật là v*cl!",
        "Call me at 123-456-7890!",
        "Liên hệ với tôi qua số 098-765-4321!",
        "<p></p>",
        "<script>alert('This is a test');</script>",
        "Content without meaning $$$ %%% @@@",
        "Nội dung không rõ nghĩa ### $$$",
        "The password is '12345'.",
        "Mật khẩu là 'abcdef'.",
        "Do not share your social security number.",
        "Không chia sẻ số chứng minh nhân dân của bạn.",
        "Buy now for $9.99 only!",
        "Mua ngay với giá chỉ 199.000đ!",
        "Vũng Tàu có bãi biển đẹp",
        "Hà Nội đẹp",
        "Đà Lạt mộng mơ",
        "Đà Lạt là thành phố du lịch nổi tiếng của Việt Nam",
        "Đà Lạt mùa này rất đẹp",
        "Đà Lạt có rất nhiều hoa",
        "Hà Nội",
        "sex",
        "mua bán trinh",
        "đẹp lắm nha",
        "Chợ",
        "Đà Lạt",
        "TP.HCM",
        "buôn bán",
        "ma túy",
        "gái",
    ],
    'label': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1,1]  # 0: Không nhạy cảm, 1: Nhạy cảm
}

# Tạo DataFrame từ dữ liệu
df = pd.DataFrame(data)

# Danh sách các địa điểm ở Việt Nam
dia_diem = [
    "Hà Nội",
    "TP.HCM",
    "Đà Nẵng",
    "Hải Phòng",
    "Cần Thơ",
    "Biên Hòa",
    "Nha Trang",
    "Huế",
    "Long Xuyên",
    "Thái Nguyên",
    "Buôn Ma Thuột",
    "Bắc Giang",
    "Bến Tre",
    "Vũng Tàu",
    "Quảng Ngãi",
    "Nam Định",
    "Thái Bình",
    "Hạ Long",
    "Sóc Trăng",
    "Vĩnh Long",
    "Cà Mau",
    "Hội An",
    "Lạng Sơn",
    "Điện Biên Phủ",
    "Bạc Liêu",
    "Lào Cai",
    "Tuy Hòa",
    "Tam Kỳ",
    "Bảo Lộc",
    "Phan Rang-Tháp Chàm",
    "Hà Tĩnh",
    "Kon Tum",
    "Bắc Ninh",
    "Quy Nhơn",
    "Thanh Hóa",
    "Phú Yên",
    "Bắc Kạn",
    "Cao Bằng",
    "Đồng Hới",
    "Hà Giang",
    "Sơn La",
    "Yên Bái",
    "Pleiku",
    "Đông Hà",
    "Hà Nam",
    "Ninh Bình",
    "Vịnh Hạ Long",
    "Phú Quốc",
    "Thái Bình",
    "Hòa Bình",
    "Lai Châu",
    "Tây Ninh",
    "Củ Chi",
    "Vũng Tàu",
]
nhaycam=["<p>du licj</p>"]
# Tạo DataFrame mới từ danh sách địa điểm
df_dia_diem = pd.DataFrame({
    'text': dia_diem,
    'label': [0] * len(dia_diem)  # Đánh nhãn 0 cho tất cả địa điểm (không nhạy cảm)
})
df_nhaycam=pd.DataFrame({
    'text': nhaycam,
    'label': [1] * len(nhaycam)  # Đánh nhãn 0 cho tất cả địa điểm (không nhạy cảm)
})

# Đọc dữ liệu hiện tại từ tệp CSV
df_existing = pd.read_csv('duLieuNhayCam.csv')

# Ghép dữ liệu mới vào dữ liệu hiện tại
df_combined = pd.concat([df_existing, df_nhaycam], ignore_index=True)

# Lưu DataFrame kết hợp vào tệp CSV
df_combined.to_csv('duLieuNhayCam.csv', index=False)
