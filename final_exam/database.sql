-- ==============================================================================
-- BÀI KIỂM TRA CUỐI MODULE: PHÁT TRIỂN ỨNG DỤNG WEB VỚI JSP & SERVLET
-- Đề tài: Hệ thống Quản lý Sản phẩm (Product Management System)
-- Học viên: DTC245200413
-- Database: product_management
-- Bảng: products
-- ==============================================================================

-- 1. Tạo Database
CREATE DATABASE IF NOT EXISTS product_management CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE product_management;

-- 2. Dọn dẹp bảng cũ nếu tồn tại
DROP TABLE IF EXISTS products;

-- 3. Tạo bảng products theo đúng yêu cầu đề bài
-- Các cột: id (PRIMARY KEY, AUTO_INCREMENT), name, price, quantity
CREATE TABLE products (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    price DOUBLE NOT NULL CHECK (price >= 0),
    quantity INT NOT NULL CHECK (quantity >= 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 4. Thêm dữ liệu mẫu ban đầu (Seed Data)
INSERT INTO products (name, price, quantity) VALUES
('MacBook Pro 16 M3 Max', 3499.00, 15),
('Dell XPS 15 9530', 2199.50, 22),
('iPhone 15 Pro Max 256GB', 1199.00, 40),
('Samsung Galaxy S24 Ultra', 1299.99, 35),
('Bàn phím cơ Keychron Q1 Pro', 199.00, 50),
('Chuột không dây Logitech MX Master 3S', 99.90, 80),
('Màn hình Dell UltraSharp U2723QE 4K', 579.00, 18),
('Tai nghe chống ồn Sony WH-1000XM5', 348.00, 25),
('iPad Pro 12.9 M2 128GB Wi-Fi', 1099.00, 30),
('Apple Watch Ultra 2 GPS + Cellular', 799.00, 20);

-- 5. Truy vấn kiểm tra dữ liệu đã thêm
SELECT * FROM products ORDER BY id ASC;
