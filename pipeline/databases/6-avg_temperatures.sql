-- runs temperatures.sql
--  temperatures.sql creates a table
-- selects rows of table  by avg_temp from temperatures
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY AVG(value) DESC;
