#台灣城市最大人口數、最小人口數、最大人口數-最小人口數
USE world;
SELECT *, `最大人口數`-`最小人口數` "人口差"
FROM (
	SELECT MAX(Population) AS `最大人口數`,MIN(Population) AS `最小人口數`
    FROM city
    WHERE CountryCode = "TWN"
) AS TW