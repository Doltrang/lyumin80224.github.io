use world;
select region,name,population
from country
where region="Southeast Asia"
and population < 2000000
union
select region,name,population
from country
where region="Eastern Asia"
and population < 1000000;