package listener;

import javax.servlet.ServletContextEvent;
import javax.servlet.ServletContextListener;
import javax.servlet.annotation.WebListener;
import javax.servlet.http.*;

@WebListener()
public class Count implements ServletContextListener,
        HttpSessionListener, HttpSessionAttributeListener {
    int count = 0;
    // Public constructor is required by servlet spec
    public Count() {
    }
    // -------------------------------------------------------
    // HttpSessionListener implementation
    // -------------------------------------------------------
    public void sessionCreated(HttpSessionEvent se) {
        System.out.println("会话创建");
        count++;
        se.getSession().setAttribute("count",count);
    }

    public void sessionDestroyed(HttpSessionEvent se) {
        System.out.println("会话销毁");
        count--;
        HttpSession session =se.getSession();
        session.setAttribute("count",count);
    }

    // -------------------------------------------------------
    // HttpSessionAttributeListener implementation
    // -------------------------------------------------------

    public void attributeAdded(HttpSessionBindingEvent sbe) {

    }

    public void attributeRemoved(HttpSessionBindingEvent sbe) {
    }

    public void attributeReplaced(HttpSessionBindingEvent sbe) {

    }
}
