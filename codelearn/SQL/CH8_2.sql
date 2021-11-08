use mydb;
create table dept3(
	`deptno` int not null,
    `dname` varchar(16) not null,
    `location` varchar(16),
    primary key(`deptno`)
)character set = "utf8mb4"