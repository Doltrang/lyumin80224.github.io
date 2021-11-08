select curdate(),curtime();
select hiredate,year(hiredate),month(hiredate),day(hiredate),
monthname(hiredate),dayname(hiredate)
from cmdev.emp
#where dayname(hiredate) like "s%"
#where dayname(hiredate) between "saturday" and "sunday"
#where dayname(hiredate)="saturday" or dayname(hiredate)="sunday"