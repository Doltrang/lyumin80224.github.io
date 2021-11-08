select county,max(PM25)"PM2.5數值"
from mydb.aqx
group by county
order by max(PM25) desc
limit 3