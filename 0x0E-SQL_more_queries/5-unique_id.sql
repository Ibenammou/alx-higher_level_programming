-- 5-unique_id.sql

-- Create the table if it doesn't exist
CREATE TABLE IF NOT EXISTS unique_id (
    id INT UNIQUE DEFAULT 1,
    name VARCHAR(256)
);

