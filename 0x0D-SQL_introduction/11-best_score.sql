-- List all records with score >= 10 in table second_table.
SELECT MAX score, name
FROM second_table
ORDER BY score ASC
HAVING score >= 10;
