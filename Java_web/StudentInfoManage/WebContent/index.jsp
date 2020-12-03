<%@ page language="java" contentType="text/html; charset=utf-8"
    pageEncoding="utf-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>学生信息管理系统登录</title>
<script type="text/javascript">
	function resetValue(){
		document.getElementById("userName").value="";
		document.getElementById("password").value="";
	}
</script>
</head>
<body>
	<div align="center" style="padding-top: 50px;">
		<form action="login" method="post">
		  <table width="78%" height="695"   cellpadding="0" cellspacing="0" background="images/login１.jpg">
		    <tr>
		      <td height="125" colspan="3"><p align="center"><font face="黑体" size="7"><strong>欢迎来到学生管理系统</strong></font></p></td>
	       </tr>
		    <tr>
		      <td width="721" height="360"></td>
		      <td width="782"><p align="center">账号：
		          <input type="text" value="${userName }" name="userName" id="userName" style="width: １９０px; height: ３４px; "/>
		        </p>
		        <p align="center"> 密码：
		          <input type="password" value="${password }" name="password" id="password" style="width: １９０x; height: ３４px; "/>
	           </p>
	      <div align="center"></div>
		        <label for="radio"></label>
		        <div align="center">
		          <p>
		            <input type="submit" value="登录" style="width: 115px; height: 49px; "/>
		            <input type="button" value="重置" onClick="resetValue()" style="width: 109px; height: 51px; "/>
	             </p>
		          <p style="height: 66px; "><font color="red">${error }</font><br>
	             </p>
	           </div></td>
		      <td width="702"></td>
	       </tr>
		    <tr>
		      <td height="139"></td>
		      <td>&nbsp;</td>
		      <td></td>
	       </tr>
	     </table>
		</form>
	</div>
	<table background="img/20140525094732_Kfamn.png" width="100%" height="256"   cellpadding="0" cellspacing="0">
    <tr>
      <td width="1889" height="254"><p align="center">COPYRIGHT  1998-2019 CYN. ALL RIGHTS RESERVED.</p>
      <p align="center"> Designed By CYN.</p></td>
    </tr>
  </table>
	
</body>
</html>