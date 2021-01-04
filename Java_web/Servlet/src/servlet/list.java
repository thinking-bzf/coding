package servlet;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.*;

public class list extends HttpServlet {
    public list() {
        super();
    }

    @Override
    public void destroy() {
        super.destroy();
    }

    @Override
    public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        this.process(request, response);
//        response.setContentType("text/html;charset=UTF-8");
        PrintWriter out = response.getWriter();
        out.println("<a href='/web/new.jsp'>new student</a>");
        out.flush();
        out.close();
    }
    private void process(HttpServletRequest req,HttpServletResponse resp) throws IOException {
        resp.setContentType("text/html");
        PrintWriter out=resp.getWriter();
        try{
            req.setCharacterEncoding("UTF-8");
            String Id = req.getParameter("id");
            String Link = req.getParameter("link");
            String Password = req.getParameter("password");
            String Role = req.getParameter("role");
            String Uid = req.getParameter("uid");
            String Username = req.getParameter("username");

            Class.forName("com.mysql.cj.jdbc.Driver");
            String url = "jdbc:mysql://localhost:3306/mydatabase?useSSL=true&characterEncoding=utf-8&serverTimezone=GMT";
            String username = "root";
            String password = "bzf123";
            Connection con = DriverManager.getConnection(url, username, password);

            String sql = "SELECT * FROM students ";
            Statement st = con.createStatement();
            ResultSet rs = st.executeQuery(sql);
            String insult = "";
            if (Id != null && Id.length() > 0) {
                insult = sql + "where id = " + Id;
                rs = st.executeQuery(insult);
            }
            if (Link != null && Link.length() > 0) {
                insult = sql + "where link = \'" + Link + "\'";
                rs = st.executeQuery(insult);
            }
            if (Password != null && Password.length() > 0) {
                insult = sql + "where pwd = \'" + Password + "\'";
                rs = st.executeQuery(insult);
            }
            if (Role != null && Role.length() > 0) {
                insult = sql + "where roles = \'" + Role + "\'";
                rs = st.executeQuery(insult);
            }
            if (Uid != null && Uid.length() > 0) {
                insult = sql + "where uid = \'" + Uid + "\'";
                rs = st.executeQuery(insult);
            }
            if (Username != null && Username.length() > 0) {
                insult = sql + "where username = \'" + Username + "\'";
                rs = st.executeQuery(insult);
            }
            if (rs == null)
                out.print("未找到结果\n");
            else {
                out.println("找到以下结果");
                out.println("<table border>");
                out.println("<tr><td>id</td><td>username</td><td>roles</td><td>uid</td><td>link</td><td>pwd</td></tr>");
                while (rs.next()) {
                    out.println("<tr>");
                    int id = rs.getInt("id");
                    String link = rs.getString("link");
                    String pwd = rs.getString("pwd");
                    String roles = rs.getString("roles");
                    String uid = rs.getString("uid");
                    String UserName = rs.getString("username");
                    out.println("<td>" + id);
                    out.println("<td>" + UserName);
                    out.println("<td>" + roles);
                    out.println("<td>" + uid);
                    out.println("<td>" + link);
                    out.println("<td>" + pwd);
                    out.println("</tr>");
                }
                out.println("</table>");
            }
            rs.close();
            st.close();
            con.close();
        }catch(Exception ex){
            ex.printStackTrace();
        }
    }

}
