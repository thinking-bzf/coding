-- 1.将01311班的全体学生的成绩置0
UPDATE Grade SET Gmark = 0 WHERE Sno IN (SELECT Sno
FROM Student
WHERE Clno = '01311') 

-- 2.删除2001级计算机软件的全体学生的选课记录
DELETE FROM Grade
WHERE Sno IN (SELECT Sno
FROM Student
WHERE Clno IN (SELECT Clno
FROM Class
WHERE Speciality = '计算机软件' AND Inyear = 2001))

-- 3.学生李勇已退学，从数据库中删除有关他的记录
DELETE FROM Grade 
WHERE Sno IN (SELECT Sno
FROM Student
WHERE Sname = '李勇')

DELETE FROM Student 
WHERE Sname = '李勇'

-- 4.对每个班，求学生的平均年龄，并将结果存入数据库
SELECT a.Clno, a.Avg_Age
INTO Age_Avg
FROM (SELECT Clno, AVG(Sage) Avg_Age
    FROM Student
    GROUP BY Clno) a