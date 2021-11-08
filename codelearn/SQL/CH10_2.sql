USE world;
SELECT `Code`,`Population`
FROM country
WHERE `Population` > (
	SELECT `Population`
	FROM country
	WHERE `Code` = 'USA'
)