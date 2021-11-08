#請找出各個洲別中哪個國家人口數最高與最少的資料，分別列出洲名、國名、人口數
USE world;

SELECT mx.Continent,mx.Population "洲人口數最大值",mn.Population "洲人口數最小值" FROM
(
SELECT Continent, Population,Name
FROM country
WHERE (Continent, Population) IN (
	SELECT Continent, MAX(Population)
	FROM country
	GROUP BY Continent
    HAVING MAX(Population) > 0
)
) mx,
(
SELECT Continent, Population,Name
FROM country
WHERE (Continent, Population) IN (
	SELECT Continent, MIN(Population)
	FROM country
    WHERE Population > 0
	GROUP BY Continent
    #HAVING MIN(Population) > 0
)
) mn
