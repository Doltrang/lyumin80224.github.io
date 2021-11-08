select *
from cmdev.emp
#where salary between 2000 and 3000
#where salary between 3000 and 2000 無法執行
where salary >= 2000 
and salary <= 3000