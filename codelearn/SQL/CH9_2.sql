USE mydb;
-- 移除索引 
#ALTER TABLE emp3
#DROP INDEX `ename_uq_index`, 
#DROP INDEX `job_index`
-- 增加索引
ALTER TABLE emp3
ADD UNIQUE `ename_uq_index` USING HASH (`ename`),
ADD INDEX `job_index` USING HASH (`job`);