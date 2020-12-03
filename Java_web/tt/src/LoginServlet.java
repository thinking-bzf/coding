import java.io.IOException;
import java.io.PrintWriter;
import java.sql.*;
import java.util.*;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


public class LoginServlet extends HttpServlet {

	/**
	 * Constructor of the object.
	 */
	public LoginServlet() {
		super();
	}

	/**
	 * Destruction of the servlet. <br>
	 */
	public void destroy() {
		super.destroy(); // Just puts "destroy" string in log
		// Put your code here
	}

	/**
	 * The doGet method of the servlet. <br>
	 *
	 * This method is called when a form has its tag value method equals to get.
	 * 
	 * @param request the request send by the client to the server
	 * @param response the response send by the server to the client
	 * @throws ServletException if an error occurred
	 * @throws IOException if an error occurred
	 */
	public void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		response.setContentType("text/html");
		PrintWriter out = response.getWriter();
		out
				.println("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01 Transitional//EN\">");
		out.println("<HTML>");
		out.println("  <HEAD><TITLE>A Servlet</TITLE></HEAD>");
		out.println("  <BODY>");
		out.print("    This is ");
		out.print(this.getClass());
		out.println(", using the GET method");
		out.println("  </BODY>");
		out.println("</HTML>");
		out.flush();
		out.close();
	}

	/**
	 * The doPost method of the servlet. <br>
	 *
	 * This method is called when a form has its tag value method equals to post.
	 * 
	 * @param request the request send by the client to the server
	 * @param response the response send by the server to the client
	 * @throws ServletException if an error occurred
	 * @throws IOException if an error occurred
	 */
	public void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
       this.process(request, response);
//		response.setContentType("text/html");
//		PrintWriter out = response.getWriter();
//		out.println("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01 Transitional//EN\">");
//		out.println("<HTML>");
//		out.println("  <HEAD><TITLE>A Servlet</TITLE></HEAD>");
//		out.println("  <BODY>");
//		out.print("    This is ");
//		out.print(this.getClass());
//		out.println(", using the POST method");
//		out.println("  </BODY>");
//		out.println("</HTML>");
//		out.flush();
//		out.close();
	}

	/**
	 * Initialization of the servlet. <br>
	 *
	 * @throws ServletException if an error occurs
	 */
	public void init() throws ServletException {
		// Put your code here
	}
	
	private void process(HttpServletRequest req,HttpServletResponse resp)
	  throws IOException{
//		String username=req.getParameter("username");
//		String password=req.getParameter("password");
//		resp.setContentType("text/html");
//		PrintWriter out=resp.getWriter();
//		out.println("<html><head><title>login</title></head>");
//		out.println("<body>username:"+username+"<br>");
//		out.println("password:"+password+"</body></html>");
//		out.flush();
		resp.setContentType("text/html");
		resp.setCharacterEncoding("gbk");
		PrintWriter out=resp.getWriter();
		try{
		   Class.forName("com.mysql.jdbc.Driver");
		   Connection con = DriverManager.getConnection ("jdbc:mysql://localhost:3306/foru?user=root&password=root");
		   Statement statement = con.createStatement();
		   ResultSet rs = statement.executeQuery("SELECT * FROM lanmu");
		   out.println("<table border>");
		   out.println("<tr><td>±àºÅ<td>Ãû³Æ<td>¸¸½Úµã");
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
		    out.flush();
		 }catch(Exception ex){
			 ex.printStackTrace();
		 }
	}

}
