#insert into mydb.tstable(area,temp)
#values("台中",32);
SET SQL_SAFE_UPDATES=0;
update mydb.tstable
set temp=33
where area="台中";
select * from mydb.tstable;