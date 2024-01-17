-- 9-cities_by_state_join.sql

-- List all cities with their corresponding states
SELECT cities.id, cities.name, states.name AS state_name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id;

