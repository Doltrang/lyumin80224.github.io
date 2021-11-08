select *
from cmdev.emp
#where hiredate between "1981-02-01" and "1981-2-28"
#where hiredate >= "1981-02-01"
#and <= "1981-2-28"
#where month(hiredate) = 2
where hiredate like"%-02-%"
#order by hiredate asc
#limit 1,2 