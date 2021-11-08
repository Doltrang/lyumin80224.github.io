#set sql_safe_updates=0;#停止安全更新限制，不會有錯誤訊息
update cmdev.travel
set counter = 2
#select * from cmdev.travel
where empno=7521
and location="DALLAS";
set sql_safe_updates=1;#啟動安全更新限制，會有錯誤訊息