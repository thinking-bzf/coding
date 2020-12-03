/*
 Navicat Premium Data Transfer

 Source Server         : sql
 Source Server Type    : SQL Server
 Source Server Version : 15002000
 Source Host           : DESKTOP-5GJST0L\SQLEXPRESS:1433
 Source Catalog        : GradeManager
 Source Schema         : dbo

 Target Server Type    : SQL Server
 Target Server Version : 15002000
 File Encoding         : 65001

 Date: 09/11/2020 22:04:56
*/


-- ----------------------------
-- Table structure for Class
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[Class]') AND type IN ('U'))
	DROP TABLE [dbo].[Class]
GO

CREATE TABLE [dbo].[Class] (
  [Clno] char(5) COLLATE Chinese_PRC_CI_AS  NOT NULL,
  [Speciality] varchar(20) COLLATE Chinese_PRC_CI_AS  NOT NULL,
  [Inyear] char(4) COLLATE Chinese_PRC_CI_AS  NOT NULL,
  [Number] smallint  NULL,
  [Monitor] char(7) COLLATE Chinese_PRC_CI_AS  NULL
)
GO

ALTER TABLE [dbo].[Class] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Records of Class
-- ----------------------------
INSERT INTO [dbo].[Class] ([Clno], [Speciality], [Inyear], [Number], [Monitor]) VALUES (N'00311', N'计算机软件', N'2000', N'120', N'2000101')
GO

INSERT INTO [dbo].[Class] ([Clno], [Speciality], [Inyear], [Number], [Monitor]) VALUES (N'00312', N'计算机应用', N'2000', N'140', N'2000103')
GO

INSERT INTO [dbo].[Class] ([Clno], [Speciality], [Inyear], [Number], [Monitor]) VALUES (N'01311', N'计算机软件', N'2000', N'220', N'2001103')
GO


-- ----------------------------
-- Uniques structure for table Class
-- ----------------------------
ALTER TABLE [dbo].[Class] ADD CONSTRAINT [UQ__Class__B1FC136795FA5170] UNIQUE NONCLUSTERED ([Clno] ASC)
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO

