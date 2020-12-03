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

 Date: 09/11/2020 22:05:04
*/


-- ----------------------------
-- Table structure for Course
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[Course]') AND type IN ('U'))
	DROP TABLE [dbo].[Course]
GO

CREATE TABLE [dbo].[Course] (
  [Cno] char(1) COLLATE Chinese_PRC_CI_AS  NOT NULL,
  [Cname] varchar(20) COLLATE Chinese_PRC_CI_AS  NOT NULL,
  [Credit] smallint  NULL
)
GO

ALTER TABLE [dbo].[Course] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Records of Course
-- ----------------------------
INSERT INTO [dbo].[Course] ([Cno], [Cname], [Credit]) VALUES (N'1', N'数据库', N'4')
GO

INSERT INTO [dbo].[Course] ([Cno], [Cname], [Credit]) VALUES (N'2', N'离散数学', N'3')
GO

INSERT INTO [dbo].[Course] ([Cno], [Cname], [Credit]) VALUES (N'3', N'管理信息系统', N'2')
GO

INSERT INTO [dbo].[Course] ([Cno], [Cname], [Credit]) VALUES (N'4', N'操作系统', N'4')
GO

INSERT INTO [dbo].[Course] ([Cno], [Cname], [Credit]) VALUES (N'5', N'数据结构', N'4')
GO

INSERT INTO [dbo].[Course] ([Cno], [Cname], [Credit]) VALUES (N'6', N'数据处理', N'2')
GO

INSERT INTO [dbo].[Course] ([Cno], [Cname], [Credit]) VALUES (N'7', N'C语言', N'4')
GO


-- ----------------------------
-- Uniques structure for table Course
-- ----------------------------
ALTER TABLE [dbo].[Course] ADD CONSTRAINT [UQ__Course__C1FE6372A0FFDE25] UNIQUE NONCLUSTERED ([Cno] ASC)
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO

