<%@ page language="java" import="java.util.*,java" pageEncoding="gbk"%>
<%
    String path = request.getContextPath();
    String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <base href="<%=basePath%>">
    
    <title>My JSP 'index.jsp' starting page</title>
    
	<meta http-equiv="pragma" content="no-cache">
	<meta http-equiv="cache-control" content="no-cache">
	<meta http-equiv="expires" content="0">    
	<meta http-equiv="keywords" content="keyword1,keyword2,keyword3">
	<meta http-equiv="description" content="This is my page">
    <meta http-equiv="Content-Type" content="text/html; charset=gbk" />
	<!--
	<link rel="stylesheet" type="text/css" href="styles.css">
	-->

  </head>
  
  <body>
    This is my Login page. <br>
    <form action="Login" method="post">
    用户名：<input type="username" name="username"/><br/>
    密码：<input type="password" name="password"/><br/>
    <input type="submit" value="submit"/>&nbsp;&nbsp;
    <input type="reset" value="reset"/><br/>
 
    </form>
  </body>
</html>
