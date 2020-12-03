-- (1) 查询每位同学所选修的课程的成绩，以及与该课程平均分的差值（正数表示高于平均分，负数表示低于平均分）
-- 输出：学号，姓名，所选课程名，与平均分的差值。（注意成绩为NULL值的处理）
--创建课程号和平均分视图
CREATE VIEW Grade_Gmark
(
    Cno,
    AvgMark
)
AS
    SELECT
        Cno, AVG(Gmark)
    FROM
        Grade
    GROUP BY
	Cno;

-- 创建学号姓名所选课程号
CREATE VIEW StudentGrade
(
    Sno,
    Sname,
    Cno,
    Gmark
)
AS
    SELECT
        s.Sno,
        s.Sname ,
        g.Cno,
        g.Gmark
    FROM
        Student s
        RIGHT JOIN Grade g ON s.Sno=g.Sno;

-- 输出学号，姓名，所选课程号，与平均分的差值
SELECT
    s.Sno,
    s.Sname,
    s.Cno,
    g.AvgMark- s.Gmark
FROM
    StudentGrade s
    JOIN Grade_Gmark g ON s.Cno = g.Cno
WHERE
	s.Gmark IS NOT NULL

-- (2)检查出Student表中和Class表中数据不一致的地方。即同时输出Student中对每个班级的统计人数与Class表班级人数。
-- 输出：班级号，班级名称，统计人数，Class表中人数（Class表中没有学生的班级也要输出）。
-- 创建学生计数的视图
CREATE VIEW StudentCount
(
    Clno,
    StuCount
)
AS
    SELECT
        Clno,
        COUNT ( Clno )
    FROM
        Student
    GROUP BY
	Clno;
-- 输出
SELECT
    c.Clno,
    c.Speciality,
    s.StuCount,
    c.Number
FROM
    Class c
    JOIN StudentCount s ON c.Clno= s.Clno