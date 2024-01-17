-- 8-cities_of_california_subquery.sql

-- List all cities of California using a subquery
SELECT * FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id;

