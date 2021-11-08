use mydb;
create  temporary table tstable2(
	ts timestamp not null default current_timestamp,
    ts2 timestamp not null default current_timestamp on update current_timestamp,
    area varchar(5) not null,
    temp int not null
)