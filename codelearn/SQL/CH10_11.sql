#請找出各個洲別中哪個國家人口數最高與最少的資料，分別列出洲名、國名、人口數
USE world;
SELECT Continent,Name,Population
FROM country as a
WHERE (Continent,Population) IN (
	SELECT Continent,MAX(Population)
    FROM country
    GROUP BY Continent
    HAVING MAX(Population) > 0
);
#UNION
SELECT Continent,Name,Population
FROM country as b
WHERE (Continent,Population) IN (
	SELECT Continent,MIN(Population)
    FROM country
    WHERE Population > 0
    GROUP BY Continent
);
#ORDER BY Continent,Population DESC

SELECT Continent,Name,Population from a inner join b on a.Continent=b.Continent