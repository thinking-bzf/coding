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

 Date: 09/11/2020 22:04:47
*/


-- ----------------------------
-- Table structure for Student
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[Student]') AND type IN ('U'))
	DROP TABLE [dbo].[Student]
GO

CREATE TABLE [dbo].[Student] (
  [Sno] char(7) COLLATE Chinese_PRC_CI_AS  NOT NULL,
  [Sname] varchar(20) COLLATE Chinese_PRC_CI_AS  NOT NULL,
  [Ssex] char(2) COLLATE Chinese_PRC_CI_AS  NOT NULL,
  [Sage] smallint  NULL,
  [Clno] char(5) COLLATE Chinese_PRC_CI_AS  NOT NULL
)
GO

ALTER TABLE [dbo].[Student] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Records of Student
-- ----------------------------
INSERT INTO [dbo].[Student] ([Sno], [Sname], [Ssex], [Sage], [Clno]) VALUES (N'2000101', N'李勇', N'男', N'20', N'00311')
GO

INSERT INTO [dbo].[Student] ([Sno], [Sname], [Ssex], [Sage], [Clno]) VALUES (N'2000102', N'刘诗晨', N'女', N'19', N'00311')
GO

INSERT INTO [dbo].[Student] ([Sno], [Sname], [Ssex], [Sage], [Clno]) VALUES (N'2000103', N'王一鸣', N'男', N'20', N'00312')
GO

INSERT INTO [dbo].[Student] ([Sno], [Sname], [Ssex], [Sage], [Clno]) VALUES (N'2001101', N'李勇敏', N'女', N'21', N'01311')
GO

INSERT INTO [dbo].[Student] ([Sno], [Sname], [Ssex], [Sage], [Clno]) VALUES (N'2001102', N'贾向东', N'男', N'20', N'01311')
GO


-- ----------------------------
-- Uniques structure for table Student
-- ----------------------------
ALTER TABLE [dbo].[Student] ADD CONSTRAINT [UQ__Student__CA1FE465C1BBD3A2] UNIQUE NONCLUSTERED ([Sno] ASC)
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO

