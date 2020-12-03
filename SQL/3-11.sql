-- 给学生表添加Nation属性 数据类型为Varchar(20)
ALTER TABLE Student
    ADD Nation VARCHAR(20);

-- 删除学生表的新增属性Nation
ALTER TABLE Student
    DROP COLUMN Nation;

-- 向成绩表中插入记录('2001110','3',30)
INSERT INTO Grade
VALUES('2001110', '3', 80);

-- 将学号为'2001110'的学生的成绩修改为70分
UPDATE Grade
SET Gmark='70'
WHERE Sno='2001110'

-- 删除学号为'2001110'的学生成绩记录
DELETE FROM Grade 
WHERE Sno ='2001110'

-- 在学生表的cno属性上创建一个名为IX_Class的索引，以班级号升序排序额
CREATE INDEX IX_Class
ON Student(Clno ASC)

-- 删除IX_Class索引
DROP INDEX Student.IX_Class

