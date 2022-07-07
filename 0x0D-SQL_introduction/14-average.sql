--- bqbqbqbqbqbq
SELECT * FROM second_table
WHERE average > (SELECT AVG(average) FROM second_table);
