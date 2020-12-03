CREATE TABLE Student
(
    Sno CHAR(7) NOT NULL UNIQUE,
    Sname VARCHAR(20) NOT NULL,
    Ssex CHAR(2) NOT NULL ,
    Sage SMALLINT NULL ,
    Clno CHAR(5) NOT NULL,
);
CREATE TABLE Course
(
    Cno CHAR(1) Not NULL UNIQUE,
    Cname VARCHAR(20) NOT NULL,
    Credit SMALLINT NULL,
);
CREATE TABLE Class
(
    Clno CHAR(5) NOT NULL UNIQUE,
    Speciality VARCHAR Not NULL,
    Inyear CHAR(4) NOT NULL,
    Number SMALLINT NULL,
    Monitor CHAR(7) NULL
);
CREATE TABLE Grade
(
    Sno CHAR(7) NOT NULL,
    Cno CHAR(1) NOT NULL,
    Gmark NUMERIC(4,1) NULL
);