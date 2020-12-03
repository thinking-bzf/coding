



-- 求每个课程号及其做相应的选课人数
SELECT joined.cno1, COUNT(joined.Sno)
FROM
    (SELECT c.Cno cno1, c.Cname, g.Cno cno2, g.Sno
    FROM Course c LEFT JOIN Grade g
        on c.Cno = g.Cno) as joined
GROUP BY joined.Cno1


-- 查询选修了三门课以上的学生学号
SELECT Sno
FROM
    (SELECT Sno, COUNT(Cno) cnt
    FROM Grade
    GROUP BY Sno) a
WHERE a.cnt >3

