-- file convert to utf8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE hbtn_0c_0
SELECT name CONVERT name USING utf8
FROM first_tabme;
