use world;
SELECT CountryCode
FROM city
WHERE Population > 9000000;
SELECT `Name`
FROM country
WHERE `code` = "IND"