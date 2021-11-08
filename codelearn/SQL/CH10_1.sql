USE world;
SELECT population
FROM country
WHERE `code` = "JPN"; #126714000
SELECT `code`,population
FROM country
WHERE population > 126714000