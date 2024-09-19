
CREATE DATABASE QLThongTinSV;

USE QLThongTinSV;
CREATE TABLE SinhVien (
  idSinhVien int PRIMARY KEY auto_increment,
hovaten varchar(50),
ngaysinh datetime,
gioitinh varchar(10),
sodienthoai varchar(12),
chungminhthu varchar(20),
email varchar(50),
noisinh varchar(50),
dantoc varchar(20),
tongiao varchar(20),
hokhau varchar(100),
trangthai int,
macv int,
makhoahoc int,
mabangdiem int,
mahinhanh int
);

CREATE TABLE KhoaHoc (
  makhoahoc int PRIMARY KEY auto_increment,
manganhhoc varchar(15),
lop varchar(10),
nganh varchar(100),
khoa varchar(100),
hedaotao varchar(100),
nienkhoa varchar(50)
);

CREATE TABLE KhoAnh (
  mahinhanh int PRIMARY KEY auto_increment,
url varchar(200)
);

CREATE TABLE NguoiCoVan (
  macv int PRIMARY KEY auto_increment,
hovaten varchar(20),
email varchar(100),
sodienthoai varchar(20)
);

CREATE TABLE ThanhTich (
  mabangdiem int PRIMARY KEY auto_increment,
bangdiemchitiet int,
hocki int,
diem FLOAT,
trangthai int
);

CREATE TABLE MonHoc (
  mamonhoc int PRIMARY KEY auto_increment,
tenmon varchar(255)
);

CREATE TABLE BangDiemChiTiet (
  mabangdiem int primary key auto_increment,
bangdiemchitiet int,
mamonhoc int,
diemgiuaki
FLOAT,
diemcuoiki FLOAT
);

ALTER TABLE SinhVien ADD FOREIGN KEY (macv) REFERENCES NguoiCoVan (macv);

ALTER TABLE SinhVien ADD FOREIGN KEY (mabangdiem) REFERENCES ThanhTich (mabangdiem);

ALTER TABLE SinhVien ADD FOREIGN KEY (makhoahoc) REFERENCES KhoaHoc (makhoahoc);

ALTER TABLE SinhVien ADD FOREIGN KEY (mahinhanh) REFERENCES KhoAnh (mahinhanh);


ALTER TABLE BangDiemChiTiet ADD INDEX idx_bangdiemchitiet (bangdiemchitiet);

ALTER TABLE ThanhTich ADD FOREIGN KEY (bangdiemchitiet) REFERENCES BangDiemChiTiet (bangdiemchitiet);

ALTER TABLE BangDiemChiTiet ADD FOREIGN KEY (mamonhoc) REFERENCES MonHoc (mamonhoc);

--

insert into MonHoc(tenmon)
values('Mạng máy tính'),
('Toán Rời Rạc'),
('Hệ Điều Hành'),
('Cấu Trúc Dữ Liệu'),
('Lập Trình Web'),
('An Toàn Thông Tin'),
('Kỹ Thuật Lập Trình'),
('Mạng Máy Tính'),
('Phân Tích Thiết Kế Hệ Thống'),
('Cơ Sở Dữ Liệu');

insert into NguoiCoVan(hovaten, email, sodienthoai)
values('Nguyễn Hồng Anh', 'honganh@gmail.com' ,'0967887546'),
('Nguyễn Kim Pha', 'phanguyen@gmail.com' ,'0966587546'),
('Nguyễn Hà Đông', 'hadong12@gmail.com' ,'0967009768');


insert into KhoaHoc(manganhhoc ,lop ,nganh ,khoa ,hedaotao ,nienkhoa)
values ('IT01', 'DH1226' ,'Công Nghệ Thông Tin', 'Công Nghệ Thông Tin', 'Đại Trà' ,'2019-2024'),
('IT02', 'DH1225' ,'Kỹ Thuật Phần Mềm', 'Công Nghệ Thông Tin', 'Đại Trà' ,'2019-2024'),
('IT03', 'DH1224' ,'Hệ Thống Thông Tin', 'Công Nghệ Thông Tin' ,'Đại Trà' ,'2019-2024');

insert into KhoAnh(url)
values('./images/22410431_LeVanTrung.png'),
('./images/22410261_PhamHuuNghia.png'),
('./images/22410341_HuynhQuangQuan.png'),
('./anhNhanDang/sinhvien4.png');

insert into BangDiemChiTiet(bangdiemchitiet ,mamonhoc ,diemgiuaki ,diemcuoiki)
values (1 ,1 ,10 ,8),
(1 ,3 ,9 ,9),
(1 ,5 ,5 ,8),
(1 ,8 ,8 ,9),
(2 ,1 ,9 ,10),
(2 ,3 ,9 ,9),
(2 ,5 ,7 ,8),
(2 ,8 ,6 ,9),
(3 ,1 ,9 ,10),
(3 ,4 ,10 ,9),
(3 ,5 ,7 ,8),
(3 ,6 ,9 ,9),
(4 ,1 ,9 ,10),
(4 ,4 ,2 ,9),
(4 ,5 ,5 ,8),
(4 ,6 ,10 ,9);

insert into ThanhTich(bangdiemchitiet ,hocki ,diem ,trangthai)
values (1 ,'1' ,null ,1),
(2 ,'1' ,null ,1),
(3 ,'1' ,null ,1),
(4 ,'1' ,null ,1);


insert into SinhVien(idsinhvien, hovaten, ngaysinh, gioitinh, sodienthoai, chungminhthu, email ,noisinh, dantoc, tongiao, hokhau, trangthai, macv, makhoahoc, mabangdiem, mahinhanh)
values ('22410431','Lê Văn Trung' ,date('2004-03-14'), 'nam', '0567810441', '060204012664', 'trungm8fordev@gmail.com', 'binh thuan', 'kinh', 'khong', 'Ham Tan - Binh Thuan', 1, 1, 1, 1, 1),
('22410261','Phạm Hữu Nghĩa' ,date('2000-09-14'), 'nam', '0786415164', '065198156117', 'phamhuunghia@gmail.com', 'HCM', 'kinh', 'khong', 'Q5 - TP.Ho Chi Minh.', 1, 2, 1, 2, 2),
('22410341','Huỳnh Quang Quân' ,date('2003-08-20'), 'nam', '0987716514', '894114154878', 'huynhquangquan@gmail.com', 'HCM', 'kinh', 'khong', 'Q5 - TP.Ho Chi Minh.', 1, 3, 1, 3, 2);

# #
# #
# #
# # #
CREATE
DATABASE
QLThongTinSV;

USE
QLThongTinSV;
CREATE
TABLE
`SinhVien`(
  `idSinhVien`
int
PRIMARY
KEY
auto_increment,
`hovaten`
varchar(50),
`ngaysinh`
datetime,
`gioitinh`
varchar(10),
`sodienthoai`
varchar(12),
`chungminhthu`
varchar(20),
`email`
varchar(50),
`noisinh`
varchar(50),
`dantoc`
varchar(20),
`tongiao`
varchar(20),
`hokhau`
varchar(100),
`trangthai`
int,
`macv`
int,
`makhoahoc`
int,
`mabangdiem`
int,
`mahinhanh`
int
);

CREATE
TABLE
`KhoaHoc`(
  `makhoahoc`
int
PRIMARY
KEY
auto_increment,
`manganhhoc`
varchar(15),
`lop`
varchar(10),
`nganh`
varchar(100),
`khoa`
varchar(100),
`hedaotao`
varchar(100),
`nienkhoa`
varchar(50)
);

CREATE
TABLE
`KhoAnh`(
  `mahinhanh`
int
PRIMARY
KEY
auto_increment,
`url`
varchar(200)
);

CREATE
TABLE
`NguoiCoVan`(
  `macv`
int
PRIMARY
KEY
auto_increment,
`hovaten`
varchar(20),
`email`
varchar(100),
`sodienthoai`
varchar(20)
);

CREATE
TABLE
`ThanhTich`(
  `mabangdiem`
int
PRIMARY
KEY
auto_increment,
`bangdiemchitiet`
int,
`hocki`
int,
`diem`
FLOAT,
`trangthai`
int
);

CREATE
TABLE
`MonHoc`(
  `mamonhoc`
int
PRIMARY
KEY
auto_increment,
`tenmon`
varchar(255)
);

CREATE
TABLE
`BangDiemChiTiet`(
  `mabangdiem`
int
primary
key
auto_increment,
`bangdiemchitiet`
int,
`mamonhoc`
int,
`diemgiuaki`
FLOAT,
`diemcuoiki`
FLOAT
);

ALTER
TABLE
`SinhVien`
ADD
FOREIGN
KEY(`macv`)
REFERENCES
`NguoiCoVan`(`macv`);

ALTER
TABLE
`SinhVien`
ADD
FOREIGN
KEY(`mabangdiem`)
REFERENCES
`ThanhTich`(`mabangdiem`);

ALTER
TABLE
`SinhVien`
ADD
FOREIGN
KEY(`makhoahoc`)
REFERENCES
`KhoaHoc`(`makhoahoc`);

ALTER
TABLE
`SinhVien`
ADD
FOREIGN
KEY(`mahinhanh`)
REFERENCES
`KhoAnh`(`mahinhanh`);

ALTER
TABLE
`BangDiemChiTiet`
ADD
INDEX
`idx_bangdiemchitiet`(`bangdiemchitiet`);

ALTER
TABLE
`ThanhTich`
ADD
FOREIGN
KEY(`bangdiemchitiet`)
REFERENCES
`BangDiemChiTiet`(`bangdiemchitiet`);

ALTER
TABLE
`BangDiemChiTiet`
ADD
FOREIGN
KEY(`mamonhoc`)
REFERENCES
`MonHoc`(`mamonhoc`);


insert into MonHoc(tenmon)
values('Mạng máy tính'),
('Toán Rời Rạc'),
('Hệ Điều Hành'),
('Cấu Trúc Dữ Liệu'),
('Lập Trình Web'),
('An Toàn Thông Tin'),
('Kỹ Thuật Lập Trình'),
('Mạng Máy Tính'),
('Phân Tích Thiết Kế Hệ Thống'),
('Cơ Sở Dữ Liệu');

insert into NguoiCoVan(hovaten, email, sodienthoai)
values('Nguyễn Hồng Anh', 'honganh@gmail.com', '0967887546'),
('Nguyễn Kim Pha', 'phanguyen@gmail.com', '0966587546'),
('Nguyễn Hà Đông', 'hadong12@gmail.com', '0967009768');

insert into KhoaHoc(manganhhoc, lop, nganh, khoa, hedaotao, nienkhoa)
values('IT01', 'DH1226', 'Công Nghệ Thông Tin', 'Công Nghệ Thông Tin', 'Đại Trà', '2019-2024'),
('IT02', 'DH1225', 'Kỹ Thuật Phần Mềm', 'Công Nghệ Thông Tin', 'Đại Trà', '2019-2024'),
('IT03', 'DH1224', 'Hệ Thống Thông Tin', 'Công Nghệ Thông Tin', 'Đại Trà', '2019-2024');

insert into KhoAnh(url)
values('./images/22410431_LeVanTrung.png'),
('./images/22410261_PhamHuuNghia.png'),
('./images/22410341_HuynhQuangQuan.png'),
('./anhNhanDang/sinhvien4.png');

insert
into
BangDiemChiTiet(bangdiemchitiet, mamonhoc, diemgiuaki, diemcuoiki)
values(1, 1, 10, 8),
(1, 3, 9, 9),
(1, 5, 5, 8),
(1, 8, 8, 9),
(2, 1, 9, 10),
(2, 3, 9, 9),
(2, 5, 7, 8),
(2, 8, 6, 9),
(3, 1, 9, 10),
(3, 4, 10, 9),
(3, 5, 7, 8),
(3, 6, 9, 9),
(4, 1, 9, 10),
(4, 4, 2, 9),
(4, 5, 5, 8),
(4, 6, 10, 9);

insert
into
ThanhTich(bangdiemchitiet, hocki, diem, trangthai)
values(1, '1', null, 1),
(2, '1', null, 1),
(3, '1', null, 1),
(4, '1', null, 1);

insert into SinhVien(idsinhvien, hovaten, ngaysinh, gioitinh, sodienthoai, chungminhthu, email ,noisinh, dantoc, tongiao, hokhau, trangthai, macv, makhoahoc, mabangdiem, mahinhanh)
values ('22410431','Lê Văn Trung' ,date('2004-03-14'), 'nam', '0567810441', '060204012664', 'trungm8fordev@gmail.com', 'binh thuan', 'kinh', 'khong', 'Ham Tan - Binh Thuan', 1, 1, 1, 1, 1),
('22410261','Phạm Hữu Nghĩa' ,date('2000-09-14'), 'nam', '0786415164', '065198156117', 'phamhuunghia@gmail.com', 'HCM', 'kinh', 'khong', 'Q5 - TP.Ho Chi Minh.', 1, 2, 1, 2, 2),
('22410341','Huỳnh Quang Quân' ,date('2003-08-20'), 'nam', '0987716514', '894114154878', 'huynhquangquan@gmail.com', 'HCM', 'kinh', 'khong', 'Q5 - TP.Ho Chi Minh.', 1, 3, 1, 3, 3);


UPDATE ThanhTich
SET diem = (
	select (AVG(ct.diemcuoiki) + AVG(ct.diemgiuaki))/2
	from BangDiemChiTiet as ct
	where ct.bangdiemchitiet =2
)
WHERE mabangdiem = 2;