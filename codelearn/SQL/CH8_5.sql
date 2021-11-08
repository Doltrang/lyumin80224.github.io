use mydb;
create table dept5(
	`deptno` int not null auto_increment,
    `dname` varchar(16) not null,
    `location` varchar(16),
    primary key(`deptno`)
)auto_increment=10,character set = "utf8mb4"