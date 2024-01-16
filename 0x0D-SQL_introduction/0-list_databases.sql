-- 0-list_databases.sql

-- This query selects all database names from the information_schema.SCHEMATA table.
-- The result is a list of databases on the MySQL server.

SELECT schema_name
FROM information_schema.SCHEMATA;
