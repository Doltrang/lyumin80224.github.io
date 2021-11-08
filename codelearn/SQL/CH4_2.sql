use world;
select country.Name, city.Name
from country,city
where country.Capital = city.ID