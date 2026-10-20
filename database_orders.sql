-- ==============================================================================
-- BÀI TẬP: XÂY DỰNG CƠ SỞ DỮ LIỆU QUẢN LÝ ĐƠN ĐẶT HÀNG VÀ PHIẾU GIAO HÀNG
-- Hệ quản trị CSDL: MySQL / MariaDB / SQL Server / PostgreSQL tương thích chuẩn ANSI SQL
-- Sinh viên thực hiện: DTC245200413
-- Repository: https://github.com/dtc245200413-cmyk/backend
-- ==============================================================================

-- 1. TẠO CƠ SỞ DỮ LIỆU
CREATE DATABASE IF NOT EXISTS QuanLyDonDatHang CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE QuanLyDonDatHang;

-- ==============================================================================
-- 2. TẠO CÁC BẢNG DANH MỤC THỰC THỂ (KHÔNG PHỤ THUỘC KHÓA NGOẠI TRƯỚC)
-- ==============================================================================

-- Bảng 1: ĐƠN VỊ KHÁCH (Đã chuẩn hóa, gộp Đơn vị đặt hàng & Đơn vị khách hàng)
CREATE TABLE DON_VI_KHACH (
    MaDV VARCHAR(20) NOT NULL PRIMARY KEY COMMENT 'Mã đơn vị khách hàng',
    TenDV NVARCHAR(100) NOT NULL COMMENT 'Tên đơn vị đặt hàng/giao hàng',
    DiaChi NVARCHAR(200) NOT NULL COMMENT 'Địa chỉ đơn vị',
    DienThoai VARCHAR(15) NULL COMMENT 'Số điện thoại liên hệ'
) ENGINE=InnoDB;

-- Bảng 2: NGƯỜI ĐẶT (Thuộc Đơn vị khách)
CREATE TABLE NGUOI_DAT (
    MaSoND VARCHAR(20) NOT NULL PRIMARY KEY COMMENT 'Mã số người đặt hàng',
    HoTenND NVARCHAR(100) NOT NULL COMMENT 'Họ và tên người đặt hàng',
    MaDV VARCHAR(20) NOT NULL COMMENT 'Thuộc Đơn vị khách',
    CONSTRAINT FK_NguoiDat_DonVi FOREIGN KEY (MaDV) 
        REFERENCES DON_VI_KHACH(MaDV) 
        ON UPDATE CASCADE 
        ON DELETE RESTRICT
) ENGINE=InnoDB;

-- Bảng 3: NGƯỜI NHẬN (Thuộc Đơn vị khách)
CREATE TABLE NGUOI_NHAN (
    MaSoNN VARCHAR(20) NOT NULL PRIMARY KEY COMMENT 'Mã số người nhận hàng',
    HoTenNN NVARCHAR(100) NOT NULL COMMENT 'Họ và tên người nhận hàng',
    MaDV VARCHAR(20) NOT NULL COMMENT 'Thuộc Đơn vị khách',
    CONSTRAINT FK_NguoiNhan_DonVi FOREIGN KEY (MaDV) 
        REFERENCES DON_VI_KHACH(MaDV) 
        ON UPDATE CASCADE 
        ON DELETE RESTRICT
) ENGINE=InnoDB;

-- Bảng 4: NGƯỜI GIAO (Nhân viên giao vận của doanh nghiệp)
CREATE TABLE NGUOI_GIAO (
    MaSoNG VARCHAR(20) NOT NULL PRIMARY KEY COMMENT 'Mã số người giao hàng',
    HoTenNG NVARCHAR(100) NOT NULL COMMENT 'Họ và tên người giao hàng'
) ENGINE=InnoDB;

-- Bảng 5: NƠI GIAO (Địa điểm giao nhận hàng hóa)
CREATE TABLE NOI_GIAO (
    MaSoDDG VARCHAR(20) NOT NULL PRIMARY KEY COMMENT 'Mã số địa điểm giao',
    TenNoiGiao NVARCHAR(200) NOT NULL COMMENT 'Tên / Địa chỉ nơi giao hàng'
) ENGINE=InnoDB;

-- Bảng 6: HÀNG HÓA
CREATE TABLE HANG_HOA (
    MaHang VARCHAR(20) NOT NULL PRIMARY KEY COMMENT 'Mã mặt hàng',
    TenHang NVARCHAR(100) NOT NULL COMMENT 'Tên mặt hàng',
    DvTinh NVARCHAR(30) NOT NULL COMMENT 'Đơn vị tính (Cái, Thùng, Kg, Bộ...)',
    MoTaHang NVARCHAR(255) NULL COMMENT 'Mô tả chi tiết mặt hàng'
) ENGINE=InnoDB;

-- ==============================================================================
-- 3. TẠO CÁC BẢNG CHỨNG TỪ VÀ BẢNG TRUNG GIAN (QUAN HỆ ĐẶT & GIAO)
-- ==============================================================================

-- Bảng 7: ĐƠN ĐẶT HÀNG (Chứng từ Đơn hàng)
CREATE TABLE DON_DAT_HANG (
    SoDH VARCHAR(20) NOT NULL PRIMARY KEY COMMENT 'Số đơn hàng',
    NgayDat DATE NOT NULL COMMENT 'Ngày lập đơn đặt hàng',
    MaSoND VARCHAR(20) NOT NULL COMMENT 'Người đại diện đặt hàng',
    CONSTRAINT FK_DonDatHang_NguoiDat FOREIGN KEY (MaSoND) 
        REFERENCES NGUOI_DAT(MaSoND) 
        ON UPDATE CASCADE 
        ON DELETE RESTRICT
) ENGINE=InnoDB;

-- Bảng 8: CHI TIẾT ĐẶT HÀNG (Quan hệ nhiều - nhiều giữa Đơn đặt hàng và Hàng hóa)
CREATE TABLE CHI_TIET_DAT_HANG (
    SoDH VARCHAR(20) NOT NULL COMMENT 'Số đơn hàng',
    MaHang VARCHAR(20) NOT NULL COMMENT 'Mã hàng',
    SoLuongDat INT NOT NULL CHECK (SoLuongDat > 0) COMMENT 'Số lượng đặt',
    PRIMARY KEY (SoDH, MaHang),
    CONSTRAINT FK_CTDH_DonDatHang FOREIGN KEY (SoDH) 
        REFERENCES DON_DAT_HANG(SoDH) 
        ON UPDATE CASCADE 
        ON DELETE CASCADE,
    CONSTRAINT FK_CTDH_HangHoa FOREIGN KEY (MaHang) 
        REFERENCES HANG_HOA(MaHang) 
        ON UPDATE CASCADE 
        ON DELETE RESTRICT
) ENGINE=InnoDB;

-- Bảng 9: PHIẾU GIAO HÀNG (Chứng từ Giao nhận)
CREATE TABLE PHIEU_GIAO_HANG (
    SoPG VARCHAR(20) NOT NULL PRIMARY KEY COMMENT 'Số phiếu giao hàng',
    NgayGiao DATE NOT NULL COMMENT 'Ngày thực tế giao hàng',
    SoDH VARCHAR(20) NOT NULL COMMENT 'Giao theo đơn đặt hàng số',
    MaSoNG VARCHAR(20) NOT NULL COMMENT 'Người thực hiện giao hàng',
    MaSoNN VARCHAR(20) NOT NULL COMMENT 'Người nhận hàng',
    MaSoDDG VARCHAR(20) NOT NULL COMMENT 'Địa điểm nơi giao hàng',
    CONSTRAINT FK_PhieuGiao_DonHang FOREIGN KEY (SoDH) 
        REFERENCES DON_DAT_HANG(SoDH) 
        ON UPDATE CASCADE 
        ON DELETE RESTRICT,
    CONSTRAINT FK_PhieuGiao_NguoiGiao FOREIGN KEY (MaSoNG) 
        REFERENCES NGUOI_GIAO(MaSoNG) 
        ON UPDATE CASCADE 
        ON DELETE RESTRICT,
    CONSTRAINT FK_PhieuGiao_NguoiNhan FOREIGN KEY (MaSoNN) 
        REFERENCES NGUOI_NHAN(MaSoNN) 
        ON UPDATE CASCADE 
        ON DELETE RESTRICT,
    CONSTRAINT FK_PhieuGiao_NoiGiao FOREIGN KEY (MaSoDDG) 
        REFERENCES NOI_GIAO(MaSoDDG) 
        ON UPDATE CASCADE 
        ON DELETE RESTRICT
) ENGINE=InnoDB;

-- Bảng 10: CHI TIẾT PHIẾU GIAO HÀNG (Lưu số lượng giao, đơn giá và thành tiền theo mặt hàng)
CREATE TABLE CHI_TIET_GIAO_HANG (
    SoPG VARCHAR(20) NOT NULL COMMENT 'Số phiếu giao hàng',
    MaHang VARCHAR(20) NOT NULL COMMENT 'Mã hàng hóa giao',
    SoLuongGiao INT NOT NULL CHECK (SoLuongGiao > 0) COMMENT 'Số lượng giao thực tế',
    DonGia DECIMAL(18, 2) NOT NULL CHECK (DonGia >= 0) COMMENT 'Đơn giá xuất bán',
    ThanhTien DECIMAL(18, 2) NOT NULL CHECK (ThanhTien >= 0) COMMENT 'Thành tiền = SoLuong * DonGia',
    PRIMARY KEY (SoPG, MaHang),
    CONSTRAINT FK_CTPG_PhieuGiao FOREIGN KEY (SoPG) 
        REFERENCES PHIEU_GIAO_HANG(SoPG) 
        ON UPDATE CASCADE 
        ON DELETE CASCADE,
    CONSTRAINT FK_CTPG_HangHoa FOREIGN KEY (MaHang) 
        REFERENCES HANG_HOA(MaHang) 
        ON UPDATE CASCADE 
        ON DELETE RESTRICT
) ENGINE=InnoDB;

-- ==============================================================================
-- 4. DỮ LIỆU MẪU THỬ NGHIỆM (SEED DATA)
-- ==============================================================================

INSERT INTO DON_VI_KHACH (MaDV, TenDV, DiaChi, DienThoai) VALUES
('DV01', N'Công ty TNHH Giải Pháp Công Nghệ CMYK', N'123 Đường Quang Trung, TP. Thái Nguyên', '0912345678'),
('DV02', N'Tập đoàn Bán lẻ FPT', N'456 Đường Cầu Giấy, Hà Nội', '0987654321');

INSERT INTO NGUOI_DAT (MaSoND, HoTenND, MaDV) VALUES
('ND01', N'Nguyễn Văn An', 'DV01'),
('ND02', N'Trần Thị Mai', 'DV02');

INSERT INTO NGUOI_NHAN (MaSoNN, HoTenNN, MaDV) VALUES
('NN01', N'Lê Minh Khang', 'DV01'),
('NN02', N'Phạm Thu Hà', 'DV02');

INSERT INTO NGUOI_GIAO (MaSoNG, HoTenNG) VALUES
('NG01', N'Hoàng Quốc Bảo'),
('NG02', N'Đỗ Tuấn Hưng');

INSERT INTO NOI_GIAO (MaSoDDG, TenNoiGiao) VALUES
('DDG01', N'Kho A - Số 123 Đường Quang Trung, TP. Thái Nguyên'),
('DDG02', N'Chi nhánh Cầu Giấy - Hà Nội');

INSERT INTO HANG_HOA (MaHang, TenHang, DvTinh, MoTaHang) VALUES
('H01', N'Máy tính xách tay Dell XPS 15', N'Chiếc', N'Core i7, 16GB RAM, 512GB SSD'),
('H02', N'Màn hình Dell UltraSharp 27 inch', N'Chiếc', N'Độ phân giải 4K, tấm nền IPS cao cấp'),
('H03', N'Bàn phím cơ không dây', N'Bộ', N'Switch Brown, kết nối Bluetooth 5.0');

INSERT INTO DON_DAT_HANG (SoDH, NgayDat, MaSoND) VALUES
('DH001', '2026-10-15', 'ND01'),
('DH002', '2026-10-18', 'ND02');

INSERT INTO CHI_TIET_DAT_HANG (SoDH, MaHang, SoLuongDat) VALUES
('DH001', 'H01', 5),
('DH001', 'H02', 5),
('DH002', 'H03', 10);

INSERT INTO PHIEU_GIAO_HANG (SoPG, NgayGiao, SoDH, MaSoNG, MaSoNN, MaSoDDG) VALUES
('PG001', '2026-10-19', 'DH001', 'NG01', 'NN01', 'DDG01');

INSERT INTO CHI_TIET_GIAO_HANG (SoPG, MaHang, SoLuongGiao, DonGia, ThanhTien) VALUES
('PG001', 'H01', 5, 25000000, 125000000),
('PG001', 'H02', 5, 12000000, 60000000);

-- Hoàn tất khởi tạo cơ sở dữ liệu!
