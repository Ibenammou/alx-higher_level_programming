-- Create database and the cities table

-- Create the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the database
USE hbtn_0d_usa;

-- Create the table if does not exist
CREATE TABLE IF NOT EXISTS cities (
	id INT AUTO_INCREMENT UNIQUE NOT NULL,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (state_id) REFERENCES states(id)
);
