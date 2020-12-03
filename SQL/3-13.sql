-- 找出李勇在同一个班级的学生信息
SELECT *
from student
WHERE (clno in (select clno
    from student
    where sname ='李勇') and Sname <> '李勇')

-- 获取所有与学生李勇有相同的选修课的学生信息
SELECT *
from student
where Sno in (SELECT Sno
From grade
where Cno in (select Cno
from grade
WHERE Sno in (Select Sno
From Student
where Sname ='李勇')))

-- 找出年龄介于学生李勇和25岁之间的学生信息(已知李勇的年龄小于25岁)
SELECT *
FROM Student
WHERE (Sage < 25 and Sage > (SELECT Sage
    FROM Student
    WHERE Sname = '李勇'))

--找出选修操作系统的学生学号和姓名
SELECT Sno, Sname
FROM Student
WHERE Sno in (SELECT Sno
FROM Grade
WHERE Cno in (SELECT Cno
FROM Course
WHERE Cname ='操作系统'))


-- 找出没有选修1号课程的所有学生姓名
SELECT Sname
FROM Student
WHERE Sno NOT IN(SELECT Sno
FROM Grade
WHERE Cno = 1)

-- 找出选修全部课程的学生姓名
SELECT Sname
FROM Student
WHERE Sno in 
(SELECT Sno
FROM
    (SELECT Sno, COUNT(Cno) cnt
    FROM Grade
    GROUP BY Sno) a
WHERE a.cnt IN (SELECT COUNT(*)
FROM Course))