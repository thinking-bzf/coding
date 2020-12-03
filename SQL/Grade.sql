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

 Date: 09/11/2020 20:22:47
*/


-- ----------------------------
-- Table structure for Grade
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[Grade]') AND type IN ('U'))
	DROP TABLE [dbo].[Grade]
GO

CREATE TABLE [dbo].[Grade] (
  [Sno] char(7) COLLATE Chinese_PRC_CI_AS  NOT NULL,
  [Cno] char(1) COLLATE Chinese_PRC_CI_AS  NOT NULL,
  [Gmark] numeric(4,1)  NULL
)
GO

ALTER TABLE [dbo].[Grade] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Records of Grade
-- ----------------------------
INSERT INTO [dbo].[Grade] ([Sno], [Cno], [Gmark]) VALUES (N'2000101', N'1', N'92.0')
GO

INSERT INTO [dbo].[Grade] ([Sno], [Cno], [Gmark]) VALUES (N'2000101', N'3', NULL)
GO

INSERT INTO [dbo].[Grade] ([Sno], [Cno], [Gmark]) VALUES (N'2000101', N'5', N'86.0')
GO

INSERT INTO [dbo].[Grade] ([Sno], [Cno], [Gmark]) VALUES (N'2000102', N'1', N'78.0')
GO

INSERT INTO [dbo].[Grade] ([Sno], [Cno], [Gmark]) VALUES (N'2000102', N'6', N'55.0')
GO

INSERT INTO [dbo].[Grade] ([Sno], [Cno], [Gmark]) VALUES (N'2000103', N'3', N'65.0')
GO

INSERT INTO [dbo].[Grade] ([Sno], [Cno], [Gmark]) VALUES (N'2000103', N'6', N'78.0')
GO

INSERT INTO [dbo].[Grade] ([Sno], [Cno], [Gmark]) VALUES (N'2000103', N'5', N'66.0')
GO

INSERT INTO [dbo].[Grade] ([Sno], [Cno], [Gmark]) VALUES (N'2001101', N'2', N'.0')
GO

INSERT INTO [dbo].[Grade] ([Sno], [Cno], [Gmark]) VALUES (N'2001101', N'4', N'.0')
GO

INSERT INTO [dbo].[Grade] ([Sno], [Cno], [Gmark]) VALUES (N'2001102', N'2', N'.0')
GO

INSERT INTO [dbo].[Grade] ([Sno], [Cno], [Gmark]) VALUES (N'2001102', N'4', N'.0')
GO

INSERT INTO [dbo].[Grade] ([Sno], [Cno], [Gmark]) VALUES (N'2000101', N'2', N'99.0')
GO

INSERT INTO [dbo].[Grade] ([Sno], [Cno], [Gmark]) VALUES (N'2000101', N'4', N'98.0')
GO

INSERT INTO [dbo].[Grade] ([Sno], [Cno], [Gmark]) VALUES (N'2000101', N'6', N'100.0')
GO

INSERT INTO [dbo].[Grade] ([Sno], [Cno], [Gmark]) VALUES (N'2000101', N'7', N'95.0')
GO

