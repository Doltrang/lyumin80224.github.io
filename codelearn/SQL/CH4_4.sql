use cmdev;
select *
from emp inner join dept
on emp.deptno = dept.deptno
#inner join 是交集