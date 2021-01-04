<%@ page contentType="text/html;charset=UTF-8" language="java" import="java.util.*" %>
<html>
  <head>
  </head>
  <body>
    <div>
      现在登陆人数
      <%
        String count;
        if(session.getAttribute("count")==null)
          count="0";
        else{
          count = session.getAttribute("count").toString();
        }
        out.println(count);

      %>
    </div>
  <a href="login.jsp">登陆</a>
  </body>
</html>
