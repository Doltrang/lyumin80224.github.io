select Continent,count(*) "國家數",sum(Population) "人口數",
sum(Population) div count(*) "平均國家人數"
from world.country
group by Continent;