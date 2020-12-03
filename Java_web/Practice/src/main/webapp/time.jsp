<%@ page language="java" import ="java.util.*" contentType="text/html;charset=utf-8"%>

<% 
    Date dnow = new Date();
    int dhours = dnow.getHours();
    int dminutes = dnow.getMinutes();
    int dseconds = dnow.getSeconds();
    out.print("<p>" + "服务器时间: " + dhours + ":" + dminutes+ ":" + dseconds+"</p>");
%>


<script>
    var dnow = new Date();
    var dhours = dnow.getHours();
    var dminutes = dnow.getMinutes();
    var dseconds = dnow.getSeconds();
    document.write("<br>浏览器时间: " + dhours + ":" + dminutes + ":" + dseconds);
</script>
