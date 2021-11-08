/*
insert into cmdev.dept(deptno,dname,location)
values(90,"IT","New Taipei")
insert into cmdev.dept(deptno,dname,location)
values(91,"IT","New Taipei"),(92,"IT","New Taipei")

update cmdev.dept
set location="Taipei",dname="IT"
where deptno=91
*/
delete from cmdev.dept
where deptno = 91
or deptno=92