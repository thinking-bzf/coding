<%@ page contentType="text/html;charset=UTF-8" import="java.util.*" language="java" %>
<html>
<head>
    <title>购物车</title>
</head>
<style>
    tr {
        width: 25px;
        text-align: center;
    }
</style>
<body>
<%
    Map<String, Integer> item;
    if (session.getAttribute("Item") != null)
        item = (Map<String, Integer>) session.getAttribute("Item");
    else
        item = new HashMap<>();
    if (item.size() > 0) {
        int cnt = 0;
        out.print("<table>");
        out.print("<tr><td>商品名</td><td>商品数量</td></tr>");
        for (String x : item.keySet()) {
            out.print("<tr><td>" + x + "</td><td>" + item.get(x) + "</td></tr>");
        }
        out.print("</table>");
    } else
        out.print("<ul>你的购物车是空的!</ul>");
%>
<input type="button" value="返回购物平台1" onclick="to(1)">
<input type="button" value="返回购物平台2" onclick="to(2)">

</body>
</html>
<script>
    function to(index) {
        window.location.href = "item" + index + ".jsp";
    }
</script>
