-- 找出所有被学生选修了的课程号
SELECT DISTINCT Sno
FROM Student

-- 找出01311班女学生的个人信息
SELECT *
FROM Student
WHERE Clno='01311' AND Ssex='女'

-- 找出01311班和01312班的学生姓名，性别，出生年月
SELECT Sname, Ssex, Sage
FROM Student
WHERE Clno='01311' OR Clno ='01312'

-- 找出所有姓李的学生的个人信息
SELECT *
FROM Student
WHERE Sname LIKE '李%'

-- 找出李勇所在班级的学生的人数
SELECT COUNT(*)
FROM Student
WHERE Clno in (SELECT Clno
FROM Student
WHERE Sname = '李勇')

-- 找出课程名为操作系统的平均成绩，最高分，最低分
SELECT MAX(Gmark) AS max_grade, MIN(Gmark) AS min_grade, AVG(Gmark) AS avg_grade
FROM Grade
WHERE Cno in (Select Cno
FROM Course
WHERE Cname = '操作系统')

-- 找出选修了课程的学生人数
SELECT count(DISTINCT Sno)
from Grade

-- 找出选修了课程操作系统的学生人数
SELECT count(sno)
from Grade
WHERE cno in (select cno
from course
where cname ='操作系统')

-- 找出2000级计算机软件班的成绩为空的学生姓名
SELECT sno, sname
FROM student
WHERE(clno in (Select clno
    from class
    where inyear ='2000') and Sno in (select Sno
    from Grade
    where Gmark is null) )