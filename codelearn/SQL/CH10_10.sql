USE world;
SELECT Continent,GNP,Name
FROM country
WHERE (Continent,GNP) IN (
	SELECT Continent,MAX(GNP)
    FROM country
    GROUP BY Continent
    HAVING MAX(GNP) > 0
)