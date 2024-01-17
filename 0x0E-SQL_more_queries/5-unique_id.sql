-- Create table unique_id

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

USE hbtn_0d_2;

CREATE TABLE IF NOT EXISTS unique_id (
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256),
);
