-- Prepares a MySQL server

CREATE DATABASE IF NOT EXISTS HomeCooker_db;
CREATE USER IF NOT EXISTS 'home_dev'@'localhost';
SET PASSWORD FOR 'home_dev'@'localhost' = PASSWORD('home_pwd');
GRANT ALL ON HomeCooker_db.* TO 'home_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'home_dev'@'localhost';
FLUSH PRIVILEGES;
