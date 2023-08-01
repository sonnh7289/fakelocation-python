
CREATE TABLE IF NOT EXISTS user (
	id_user	INTEGER,
	link_avatar	TEXT,
	full_name	TEXT,
	user_name	TEXT,
	ip_register	TEXT,
	check_online	TEXT,
	device_register	TEXT,
	PRIMARY KEY(id_user)
);
CREATE TABLE IF NOT EXISTS fakelocation_Image (
	linkImage	TEXT,
	id_image	INTEGER,
	device_post_image	TEXT,
	ip_location_post	TEXT,
	noi_dung	TEXT,
	id_user	INTEGER,
	user_name TEXT
	PRIMARY KEY(id_image)
);
CREATE TABLE IF NOT EXISTS comment_image (
	id_comment	INTEGER,
	id_user	INTEGER,
	id_image_post	INTEGER,
	ip_comment	TEXT,
	device_comment	INTEGER,
	noidung_comment	TEXT,
	image_link	TEXT,
	PRIMARY KEY(id_comment)
);
COMMIT;
