<%@ page language = "java" contentType = "text/html;charset=utf-8" %>
<html>

    <body>
        <h1><% out.print("hallo ");%></h1>
        <br>
        <%! 
            int number=0;     
            
            synchronized void countPeople() { 
        	   number++;
             }
        %>
        <% countPeople(); %>
        <p>你是第<% out.print(number); %>个访问本站的用户</p>
    </body>

</html>
