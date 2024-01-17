-- Create a database then create a table in it

-- Create the database if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- use the database
USE hbtn_0d_usa;

-- Create the table if it does not exist
CREATE TABLE IF NOT EXISTS states (
	id INT AUTO_INCREMENT UNIQUE NOT NULL,
	name VARCHAR(256) NOT NULL
);
