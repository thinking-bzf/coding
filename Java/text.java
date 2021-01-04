import javax.servlet.http.HttpSessionAttributeListener;
import javax.servlet.http.HttpSessionBindingEvent;
public class UserListener implements HttpSessionAttributeListener {
//用户登录身份证
 private String USERNAME;
 private UserList u1 = UserList.getInstance(); 
 
 //判断用户是否存在
 public boolean IsExist(String sfz)throws Exception
 {
 try
 {
 
 return u1.IsExist(sfz);
 }
 catch(Exception ex)
 {
 ex.printStackTrace();
 return false;
 }
 }
 
public String getUSERNAME() {
 return USERNAME;
}
public void setUSERNAME(String username) {
 USERNAME = username;
}
public void attributeAdded(HttpSessionBindingEvent event) {
 try{
 if("USERNAME".equals(event.getName())){
 u1.addUser((String)event.getValue());
 }
 }catch(Exception e){
 e.printStackTrace();
 }
 
}
public void attributeRemoved(HttpSessionBindingEvent event) {
 try{
 if("USERNAME".equals(event.getName())){
 u1.RemoveUser((String)event.getValue());
 }
 }catch(Exception e){
 e.printStackTrace();
 }
 
}
public void attributeReplaced(HttpSessionBindingEvent arg0) {
 // TODO Auto-generated method stub
 
}
}
import java.util.Enumeration;
import java.util.Iterator;
import java.util.Vector;
public class UserList {
private static final UserList userList = new UserList();
 private Vector v = new Vector();
 private int maxUser;
 
 private UserList()
 {
 //v = new Vector();
 }
 public static UserList getInstance()
 {
 return userList;
 }
 //将用户登陆身份证保存到Vector中
 public void addUser(String sfz) throws Exception
 {
 try{
 if ( sfz != null&&!"".equals(sfz))
 {
 if ( v.indexOf(sfz) >= 0)//判断是否已经存在
 return ; 
 //可能的操作
 //添加登录ID
 v.addElement(sfz);
 if(getUserCount()>maxUser){
 maxUser=getUserCount();
 }
 }
 }
 catch(Exception ex)
 {
 ex.printStackTrace(); 
 }
 finally{
 }
 }
 
 public boolean IsExist(String sfz)throws Exception
 {
 try{
 if ( v.indexOf(sfz) >= 0)
 return true; 
 return false;
 }
 catch(Exception ex)
 {
 ex.printStackTrace();
 return false;
 }
 }
 
 //删除用户登录ID
 public void RemoveUser(String sfz)throws Exception
 {
 try{
 if ( sfz != null&&!"".equals(sfz) )
 { 
 //修改数据库
 //移除用户登录ID
 v.removeElement(sfz);
 }
 }
 catch(Exception ex)
 { 
 ex.printStackTrace(); //写日志
 }
 finally{
 }
 }
 //返回Vector枚举
 public Enumeration getUserList()
 {
 return v.elements();
 }
 //返回迭代器
 public Iterator getUserListItera(){
 return v.iterator();
 }
 //返回在线人数
 public int getUserCount()
 {
 return v.size();
 }
 //返回在线人数峰值
 public int getMaxUser(){
 return maxUser;
 }
}
最后在web-xml里 加入如下信息
<listener>
 <listener-class>
 com.myxmu.listener.UserListener
 </listener-class>
</listener>