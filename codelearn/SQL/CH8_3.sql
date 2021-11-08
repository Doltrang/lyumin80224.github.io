use mydb;
create table dept4(
	`deptno` int not null,
    `dname` varchar(16) not null,
    `location` varchar(16),
    `counter` tinyint unsigned,
    `counter2` tinyint zerofill,
    `counter3` tinyint,
    primary key(`deptno`)
)character set = "utf8mb4"