CREATE DATABASE IF NOT EXISTS phptest CHARACTER SET utf8 COLLATE utf8_general_ci;

CREATE TABLE IF NOT EXISTS employee
(
emp_id VARCHAR(200),
emp_salary FLOAT,
PRIMARY KEY (emp_id)

)

CREATE USER IF NOT EXISTS 'phpadmin' IDENTIFIED BY 'phpadmin';
GRANT ALL ON phptest.* TO 'phpadmin'@'%' IDENTIFIED BY 'phpadmin';
GRANT ALL ON phptest.* TO 'phpadmin'@'localhost' IDENTIFIED BY 'phpadmin';
FLUSH PRIVILEGES;




