-- script to list all the cities of a state that can be found in database

-- Use the database
USE hbtn_0d_usa;

-- Select all the cities of the state without joining
SELECT *
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
