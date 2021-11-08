#use cmdev;
select *, salary*12 as "年薪" ,salary*12+salary div 2 "年薪(含獎金)",salary*12.5,salary*12+salary/2
from cmdev.emp;