<%@ page language="java" import="java.util.*,java.sql.*" pageEncoding="gbk"%>
<%@page import="com.mysql.jdbc.Driver"%>
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
    This is my lanmu table <br>
    <form action="index.jsp">
         编号：<input type="text" name="iid"/>
     <input type="submit"/>
    </form>
   <%  
   String conent=request.getParameter("iid");
   String sql="";
   if(conent!=null)
    sql="";
   Class.forName("com.mysql.jdbc.Driver");
   Connection con = DriverManager.getConnection ("jdbc:mysql://localhost:3306/foru?user=root&password=root");
   Statement statement = con.createStatement();
   ResultSet rs = statement.executeQuery("SELECT * FROM lanmu");
   out.println("<table border>");
      out.println("<tr><td>编号<td>名称<td>父节点");
   while(rs.next())
     {    out.println("<tr>");
		int id = rs.getInt("id");
		String lname = rs.getString("lname");
		int ifather = rs.getInt("lfather");
        out.println("<td>" + id);
        out.println("<td>" + lname);
        out.println("<td>" + ifather);
        
    out.println("</tr>");
      }
         out.println("</table>");
   %>
  </body>
</html>
