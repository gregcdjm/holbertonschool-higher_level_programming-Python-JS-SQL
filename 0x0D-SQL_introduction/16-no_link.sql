-- script that lists all records of the tabl
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
