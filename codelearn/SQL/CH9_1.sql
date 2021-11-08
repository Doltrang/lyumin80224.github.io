USE mydb;
-- 建立資料表並加入索引
CREATE TABLE `emp3` (
  `empno` int NOT NULL,
  `ename` varchar(16) NOT NULL,
  `job` varchar(16) DEFAULT NULL,
  `manager` int DEFAULT NULL,
  `hiredate` date DEFAULT NULL,
  `salary` float(7,2) DEFAULT NULL,
  `comm` float(7,2) DEFAULT NULL,
  `deptno` int DEFAULT NULL,
  PRIMARY KEY (`empno`),
  UNIQUE `ename_uq_index` (`ename`),
  INDEX `job_index` (`job`)
) ENGINE=InnoDB DEFAULT CHARSET=big5