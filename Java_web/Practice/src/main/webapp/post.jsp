<%@ page language="java" import="java.util.*" contentType="text/html;charset=UTF-8" %>
<!DOCTYPE html>
<html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=, initial-scale=1.0">
        <title>提交数据</title>
    </head>

    <body>
        <%
            // 设置编码
            request.setCharacterEncoding("UTF-8");
            // out.println("用户名: "+request.getParameter("username")+"<br>");
            // out.println("密码: "+request.getParameter("password")+"<br>");
            // out.println("籍贯: "+request.getParameter("jiguan")+"<br>");
            // out.println("出生年月: "+request.getParameter("birth")+"<br>");
            // out.println("性别: "+request.getParameter("sex")+"<br>");
            // out.println("身高: "+request.getParameter("height")+"<br>");
            // out.println("爱好: "+request.getParameter("habit")+"<br>");
            // out.println("邮箱: "+request.getParameter("email")+"<br>");
            // out.println("手机: "+request.getParameter("phonenumber")+"<br>");
            // out.println("自我介绍: "+request.getParameter("introduce")+"<br>");
            // out.println("getContentLength()="+request.getContentLength()+"<br>");
            // out.println("getContentType()="+request.getContentType()+"<br>");
            // out.println("getRequestURI()="+request.getRequestURI()+"<br>");
            // out.println("getServerPort()="+request.getServerPort()+"<br>");
            // out.println("getServerName()="+request.getServerName()+"<br>");
            // out.println("getProtocol()="+request.getProtocol()+"<br>");
            // out.println("getRemoteAddr()="+request.getRemoteAddr()+"<br>");
            // out.println("getHeaderNames()="+request.getHeaderNames()+"<br>");
            // out.println("getMethod()="+request.getMethod()+"<br>");
            // out.println("getServletPath()="+request.getServletPath()+"<br>");
            // out.println("isRequestedSessionIdValid()="+request.isRequestedSessionIdValid()+"<br>");

            String current_param = "";
            request.setCharacterEncoding("UTF-8");
            Enumeration params = request.getParameterNames();
            while(params.hasMoreElements()) {
                current_param = (String)params.nextElement();
                out.println(current_param + ":");
                out.println(request.getParameter(current_param) + "<br>");
            }
            <!-- response.setContentType("application/msword;charset=GB2312"); -->

        %>
    </body>

</html>
