-- this will list all the records of table second_table that has a name value in my MySQL server
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC;
