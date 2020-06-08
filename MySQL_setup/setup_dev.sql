-- Prepares a MySQL server

CREATE DATABASE IF NOT EXISTS HomeCooker;
CREATE USER IF NOT EXISTS 'home_dev'@'localhosts' IDENTIFIED BY 'home_pwd';
GRANT ALL PRIVILEGES ON 'homecooker_dev'.* TO 'home_dev'@'localhosts';
GRANT SELECT ON 'performance_schema'.* TO 'home_dev'@'localhosts';
FLUSH PRIVILEGES;
