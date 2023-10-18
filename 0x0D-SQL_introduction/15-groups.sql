-- this will list the amount of records with the same score in table second_table in my MySQL server
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
