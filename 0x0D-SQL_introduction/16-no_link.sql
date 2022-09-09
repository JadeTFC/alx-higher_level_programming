-- List all records of the table second_table.
SELECT(*) name
FROM second_table
GROUP BY score, name
ORDER BY name DESC;
