-- script to list all cities contained in the database

-- Use the database
USE hbtn_0d_usa;

-- Select all cities with their corresponding names using join
SELECT cities.id, cities.name, states.name
FROM cities
LEFT JOIN states ON cities.state_id = states.id
ORDER BY cities.id;
