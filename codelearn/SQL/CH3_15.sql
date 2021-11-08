select *,dayname(hiredate)"星期"
from cmdev.emp
#where dayname(hiredate) like "s%"
#where dayname(hiredate) between "saturday" and "sunday"
#where dayname(hiredate)="saturday" or dayname(hiredate)="sunday"
#where dayname(hiredate)="saturday" || dayname(hiredate)="sunday"
#where left(dayname(hiredate),1)="S"
where dayname(hiredate) in ("saturday","sunday")