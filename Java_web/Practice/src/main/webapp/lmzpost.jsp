<%@ page contentType="text/html;charset=GBK" %>
<%
    request.setCharacterEncoding("GBK");
    String Pusername = "";
    String Ppassword = "";
    Pusername = request.getParameter("username");
    Ppassword = request.getParameter("password");
%>
������<%=Pusername%><br>`
���룺<%=Ppassword%>
