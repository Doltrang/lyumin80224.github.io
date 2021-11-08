select *,dayname(hiredate)"星期",
dayofweek(hiredate)
from cmdev.emp;
select dayofyear(curdate()),quarter(curdate()),
hour(curtime()),minute(curtime()),second(curtime())