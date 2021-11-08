USE world;
SELECT `Name`
FROM country
WHERE `Code` IN (
	SELECT CountryCode
	FROM city
	WHERE Population > 8000000
)