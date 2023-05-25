-- creates a table called first_table in the current database
-- first_table description: id INT, name VARCHAR(256)
-- database name will be passed as argument of mysql command
-- SELECT or SHOW statements not allowed
CREATE TABLE IF NOT EXISTS first_table (
  id INT, 
  name VARCHAR(256)
);

