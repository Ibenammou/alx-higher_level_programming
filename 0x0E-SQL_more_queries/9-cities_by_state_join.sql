-- 9-cities_by_state_subquery.sql

-- List all cities with their corresponding states using subqueries
SELECT
  cities.id,
  cities.name,
  (SELECT states.name FROM states WHERE states.id = cities.state_id) AS state_name
FROM cities
ORDER BY cities.id;

