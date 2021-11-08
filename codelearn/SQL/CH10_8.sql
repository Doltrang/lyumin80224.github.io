INSERT INTO mydb.tw_city
(
	SELECT *
    FROM world.city
    WHERE CountryCode = "TWN"
)