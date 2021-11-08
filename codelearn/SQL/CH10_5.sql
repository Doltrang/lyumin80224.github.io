USE world;
SELECT *
FROM (
	SELECT *
    FROM city
    WHERE CountryCode = "TWN"
) AS TW
WHERE Population > 500000