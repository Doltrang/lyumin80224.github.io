USE mydb;
-- 建立索引 
CREATE UNIQUE INDEX `ename_uq_index` ON emp3(`ename`);
CREATE INDEX `job_index` ON emp3(`job`);