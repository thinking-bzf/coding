<%@ page contentType="text/html;charset=UTF-8" language="java" import="java.sql.*,java.util.*" %>
<html>
<head>
    <title>new</title>
</head>
<body>


<form action="confirm" method="get" name="student">
    <table>
        <tr>
            <td>id</td>
            <td>
                <input type="text" name="id" placeholder="请输入id" onblur="checkId()">
            </td>
            <td>
                <span id="idspan"></span>
            </td>
        </tr>
        <tr>
            <td>link</td>
            <td>
                <input type="text" name="link" placeholder="请输入link">
            </td>
        </tr>
        <tr>
            <td>password</td>
            <td>
                <input type="text" name="password" placeholder="请输入密码" onblur="checkPwd()">
            </td>
            <td>
                <span id="pwdspan">要求6-8位，首位为字母，后面5-7位是数字</span>
            </td>
        </tr>
        <tr>
            <td>role</td>
            <td>
                <input type="text" name="role" placeholder="请输入身份">
            </td>
        </tr>
        <tr>
            <td>uid</td>
            <td>
                <input type="text" name="uid" placeholder="请输入uid">
            </td>
        </tr>
        <tr>
            <td>username</td>
            <td>
                <input type="text" name="username" placeholder="请输入username">
            </td>
        </tr>
        <tr>
            <td><input type="submit" value="提交" onclick="return check()"></td>
            <td><input type="reset" value="重置"></td>
        </tr>
    </table>
</form>
<script>
    function check() {
        const link = document.forms["student"]["link"].value;
        const pwd = document.forms["student"]["password"].value;
        const role = document.forms["student"]["role"].value;
        const uid = document.forms["student"]["uid"].value;
        const username = document.forms["student"]["username"].value;
        if (pwd.length <= 0)
            alert("请输入密码");
        if (checkId() && link.length <= 255 && checkPwd() && role.length <= 255 && uid.length <= 255 && username.length <= 255) {
            alert("提交成功");
            return true;
        }
        return false;
        
    }
    
    function setInfo(id, info) {
        document.getElementById(id).innerText = info;
    }
    
    function checkId() {
        const id = document.forms["student"]["id"].value;
        const num = id.length;
        const str = /^\d{8}$/;
        if (str.test(id)) {
            setInfo("idspan", "id合规");
            return true;
        } else {
            if (num == 0) {
                setInfo("idspan", "id不能为空");
                return false;
            }
            if (num != 8)
                setInfo("idspan", "长度不符");
            else
                setInfo("idspan", "不能有数字以外的字符")
            return false;
        }
        return false;
    }
    
    function checkPwd() {
        //获取用户获得用户名信息
        const upwd = document.forms["student"]["password"].value;
        //创建校验规则,密码要求6-8位，首位为字母，后面5-7位是数字
        const reg = /^[a-z]\w{5,7}$/;
        //开始交验
        if (upwd === ""){
            setInfo("pwdspan", "密码要求6-8位，首位为字母，后面5-7位是数字");
            return false;
        }
        if (upwd == null) {
            //输入校验结果
            setInfo("pwdspan", "密码不能为空");
            return false;
        } else if (reg.test(upwd)) {
            //输入校验结果
            setInfo("pwdspan", "密码通过");
            return true;
        } else {
            //输入校验结果
            setInfo("pwdspan", "密码格式不符");
            return false;
        }
    }
</script>
</body>
</html>
