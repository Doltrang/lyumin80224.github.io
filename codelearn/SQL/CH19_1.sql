#SHOW GLOBAL VARIABLES LIKE '%secure%';
SELECT "empno","ename","job","manager","hiredate","salary","comm","deptno"
UNION
SELECT *
INTO OUTFILE "E:\\workspace\\SQL\\emp.csv"
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
FROM cmdev.emp