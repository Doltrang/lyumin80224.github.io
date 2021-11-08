use cmdev;
select *
from emp left outer join dept
on emp.deptno = dept.deptno
union
select *
from emp right outer join dept
on emp.deptno = dept.deptno;