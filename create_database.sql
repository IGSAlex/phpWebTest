CREATE DATABASE IF NOT EXISTS phptest CHARACTER SET utf8 COLLATE utf8_general_ci;


CREATE USER IF NOT EXISTS 'phpadmin' IDENTIFIED BY 'phpadmin';
GRANT ALL ON phptest.* TO 'phpadmin'@'%' IDENTIFIED BY 'phpadmin';
GRANT ALL ON phptest.* TO 'phpadmin'@'localhost' IDENTIFIED BY 'phpadmin';
FLUSH PRIVILEGES;




