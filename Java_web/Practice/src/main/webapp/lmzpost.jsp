<%@ page contentType="text/html;charset=GBK" %>
<%
    request.setCharacterEncoding("GBK");
    String Pusername = "";
    String Ppassword = "";
    Pusername = request.getParameter("username");
    Ppassword = request.getParameter("password");
%>
аеУћЃК<%=Pusername%><br>`
УмТыЃК<%=Ppassword%>
