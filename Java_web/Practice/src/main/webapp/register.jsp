<%@ page language="java" import="java.util.*" contentType="text/html;charset=utf-8"%>
<!-- <%@ page language="java" import="java.util.*" contentType="text/html;charset=utf-8"%> -->
<!DOCTYPE html>

<html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>用户注册</title>
    </head>

    <body>
        <form action="post.jsp" method="POST" name="register">
            <table>
                <tr>
                    <td>用户名</td>
                    <td>
                        <input type="text" name="username" placeholder="请输入用户名" required="required">
                    </td>
                </tr>
                <tr>
                    <td>密码</td>
                    <td>
                        <input type="password" name="password" placeholder="请输入密码" required="required">
                    </td>
                </tr>
                <tr>
                    <td>籍贯</td>
                    <td>
                        <select name="jiguan" required="required">
                            <option value="北京">北京</option>
                            <option value="上海">上海</option>
                            <option value="杭州">杭州</option>
                        </select>
                    </td>
                </tr>
                <tr>
                    <td>出生年月</td>
                    <td><input type="text" name="birth" placeholder="2000-01" required="required"></td>
                </tr>
                <tr>
                    <td>性别</td>
                    <td>
                        <input type="radio" name="sex" required="required" value="男">男
                        <input type="radio" name="sex" required="required" value="女">女
                    </td>
                </tr>
                <tr>
                    <td>身高</td>
                    <td>
                        <input type="text" name="height" placeholder="请输入身高">
                    </td>
                </tr>
                <tr>
                    <td>爱好</td>
                    <td>
                        <input type="text" name="habit">
                    </td>
                </tr>
                <tr>
                    <td>邮箱</td>
                    <td>
                        <input type="text" name="email" placeholder="请输入邮箱" required="required">
                    </td>
                </tr>
                <tr>
                    <td>手机</td>
                    <td>
                        <input type="text" name="phonenumber" placeholder="请输入手机号" required="required">
                    </td>
                </tr>
                <tr>
                    <td>自我介绍</td>
                    <td>
                        <textarea name="introduce" cols="30" rows="10" placeholder="自我介绍"></textarea>
                    </td>
                </tr>
                <tr>
                    <td><input type="submit" value="提交" onclick="return result()"></td>
                    <td><input type="reset" value="重置"></td>
                </tr>
            </table>
        </form>
    </body>
    <script>
        function checkname() {
            var name = document.forms["register"]["username"].value;
            var reg = /[a-zA-Z]/;
            if (name.length < 6 || name.length > 10) {
                alert("用户名长度与格式不符");
                return false;
            }
            else if (!reg.test(name)) {
                alert("第一个必须是字母");
                return false;   
            }
            return true;
        }
        function checkemail() {
            var e_mail = document.forms["register"]["email"].value;
            var reg = /@/;
            if (!reg.test(e_mail)) {
                alert("邮箱格式出错");
                return false;
            }
            return true;
        }
        function checkphone() {
            var number = document.forms["register"]["phonenumber"].value;
            if (number.length != 11) {
                alert("电话号码长度出错");
                return false;
            }
            return true;
        }
        function result() {
            if (checkname() && checkemail() && checkphone()) {
                document.forms["register"].submit();
                alert("提交成功");
                return true;
            }
            else
                return false;
        }
    </script>

</html>
