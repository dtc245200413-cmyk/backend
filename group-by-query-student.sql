-- ==============================================================================
-- BÀI THỰC HÀNH: LUYỆN TẬP SỬ DỤNG CÁC HÀM VÀ GROUP BY TRONG MYSQL
-- File: group-by-query.sql
-- Cơ sở dữ liệu: QuanLySinhVien
-- ==============================================================================

USE QuanLySinhVien;

-- 1. Hiển thị tất cả các thông tin môn học (bảng Subject) có credit lớn nhất
SELECT 
    SubID, 
    SubName, 
    Credit, 
    Status 
FROM Subject
WHERE Credit = (
    SELECT MAX(Credit) 
    FROM Subject
);


-- 2. Hiển thị các thông tin môn học có điểm thi lớn nhất
SELECT 
    sub.SubID, 
    sub.SubName, 
    sub.Credit, 
    sub.Status, 
    m.Mark AS MaxMark
FROM Subject sub
JOIN Mark m ON sub.SubID = m.SubID
WHERE m.Mark = (
    SELECT MAX(Mark) 
    FROM Mark
);


-- 3. Hiển thị các thông tin sinh viên và điểm trung bình của mỗi sinh viên,
-- xếp hạng theo thứ tự điểm giảm dần
SELECT 
    s.StudentID, 
    s.StudentName, 
    s.Address, 
    s.Phone, 
    ROUND(AVG(m.Mark), 2) AS AvgMark
FROM Student s
JOIN Mark m ON s.StudentID = m.StudentID
GROUP BY s.StudentID, s.StudentName, s.Address, s.Phone
ORDER BY AvgMark DESC;
