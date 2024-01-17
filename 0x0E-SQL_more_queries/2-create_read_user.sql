-- script to create database hbtn_0d_2 and user user_0d_2

-- Create database if not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create user if not exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant usage to user
GRANT USAGE ON *.* TO 'user_0d_2'@'localhost';

-- Grant select privilege only on database to user
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- flush privileges to apply the changes
FLUSH PRIVILEGES;
