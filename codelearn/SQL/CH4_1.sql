select * from world.country;
select * from world.city;
#笛卡爾乘積
select *
from world.country,world.city
where world.country.Capital = world.city.ID