-- List all records of table
-- Exclude rows without a name value
-- Display the score and the name (in this order)
-- Order records by descending score
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
