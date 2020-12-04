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

public class confirm extends HttpServlet {
    public confirm() {
        super();
    }

    @Override
    public void destroy() {
        super.destroy();
    }
    @Override
    public void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        this.process(request, response);
        response.setContentType("text/html;charset=UTF-8");
        PrintWriter out = response.getWriter();
        out.println("<a href='/web/confirm'>查看学生</a>");
        out.flush();
        out.close();
    }

//    @Override
//    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
//        super.doPost(req, resp);
//        this.doGet(req,resp);
//    }

    private void process(HttpServletRequest req, HttpServletResponse resp) throws IOException{
        resp.setContentType("text/html");
        PrintWriter out = resp.getWriter();
        out.println("success");
            req.setCharacterEncoding("UTF-8");
            String Id = req.getParameter("id");
            String Link = "\"" + req.getParameter("link") + "\"";
            String Password = "\"" + req.getParameter("password") + "\"";
            String Role = "\"" + req.getParameter("role") + "\"";
            String Uid = "\"" + req.getParameter("uid") + "\"";
            String Username = "\"" + req.getParameter("username") + "\"";
//            out.println(Username);
        System.out.println(Username);


            try{

                Class.forName("com.mysql.cj.jdbc.Driver");
                String url = "jdbc:mysql://localhost:3306/mydatabase?useSSL=true&characterEncoding=utf-8&serverTimezone=GMT";
                String username = "root";
                String password = "bzf123";
                Connection con = DriverManager.getConnection(url, username, password);
                Statement st = con.createStatement();
                ResultSet rs = st.executeQuery("SELECT id from students;");
                int flag = 1; //用来表示是否重复
                while (rs.next()) {
                    if (rs.getInt("id") == Integer.parseInt(Id))
                        flag = 0;
                }
                if (flag == 1) {
                    if (Link.length() == 0)
                        Link = "NULL";
                    if (Role.length() == 0)
                        Role = "NULL";
                    if (Uid.length() == 0)
                        Uid = "NULL";
                    if (Username.length() == 0)
                        Username = "NULL";
                    String sql = "INSERT into students value (" + Id + "," + Link + "," + Password + "," + Role + "," + Uid + "," + Username + ")";


                    st.executeUpdate(sql);
//                    out.println("添加成功。三秒返回list.jsp");
                } else
                    out.println("Id 已存在");

            }catch (Exception e) {
                out.println("<h3>Insert failed</h3>");
                e.printStackTrace();
            }
            String t = 5 + ";URL="+"/web/new.jsp";
            resp.setHeader("Refresh", t);


        out.flush();
        out.close();
    }

}
