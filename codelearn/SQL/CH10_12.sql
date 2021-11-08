USE world;
SELECT *
FROM country
WHERE EXISTS (
	SELECT *
    FROM city
    WHERE CountryCode = Country.Code
    AND Population > 8000000
)