insert into cmdev.travel(empno,location,counter)
values (7900,"BOSTON",1)
on duplicate key update counter=counter+1