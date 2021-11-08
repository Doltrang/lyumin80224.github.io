#找出各個州別中，哪個國家GNP最高的資料，分別要洲別、國名、GNP
USE world;
SELECT Continent,MAX(GNP),Name
FROM country
GROUP BY Continent;
SELECT Continent,GNP,Name
FROM country
WHERE (Continent,GNP) = ("Asia", 3787042.00)