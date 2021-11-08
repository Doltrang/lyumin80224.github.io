select Continent,count(Continent) "國家數",count(*) "國家數",count(Code)
from world.country
group by Continent;
select *
from world.country