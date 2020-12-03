<!DOCTYPE html>
<html lang="en">

    <head>
        <meta http-equiv="Content-Type" content="text/html" charset="UTF-8" />
        <title>
            Login
        </title>
    </head>
    <script type="text/javascript">
        function check() {
            var name = document.forms['form']['username'].value;
            var name_check = /^[a-zA-Z][-_a-zA-Z0-9]{6,10}/;

            var email = document.forms['form']['emailAddress'].value;
            var email_check = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+((\.[a-zA-Z0-9_-]{2,3}){1,2})$/;

            var phone_number = document.forms['form']['phoneNumber'].value;

            if (name.length <= 0 || !name_check.test(name)) {
                alert("Username must start with letters!");
                return false;
            }
            else if (name.length > 10 || name.length < 6) {
                alert("Username is too long or too short!");
                return false;
            }
            else if (email == "" || !email_check.test(email)) {
                alert("Please input the correct Email Address!");
                return false;
            }
            else if (phone_number.length != 11 || phone_number == "") {
                alert("Please input the correct phone number!");
                return false;
            }
            return true;
        }

        function result() {
            if (check()) {
                document.forms['form'].submit();
                alert("Register success!");
                return true;
            }
            else
                return false;
        }
    </script>

    <body>
        <form name="form" action="lmzpost.jsp" method="post">
            <h1>Register</h1>
            Username:<br>
            <input style="width: 300px" type="text" name="username">
            <br>
            Password:<br>
            <input style="width: 300px" type="password" name="password">
            <br>
            Hometown:<br>
            <select name="hometownSelect">
                <option value="1" name="Guangdong">Guangdong</option>
                <option value="2" name="Zhejiang">Zhejiang</option>
                <option value="3" name="Gansu">Gansu</option>
            </select>
            <br>
            Birthday:<br>
            <input style="width: 150px" type="text" name="birthYear" value="Year">
            <input style="width: 150px" type="text" name="birthMonth" value="Month">
            <br>
            Gender:<br>
            <select name="sex">
                <option value="1">Male</option>
                <option value="2">Female</option>
                <option value="3">Others</option>
            </select>
            <br>
            Hobbies:<br>
            <input style="width: 300px" type="text" name="hobbies">
            <br>
            Height:<br>
            <input style="width: 300px" type="text" name="height">
            <br>
            Email Address:<br>
            <input style="width: 300px" type="text" value="user@xxx.com" name="emailAddress">
            <br>
            Phone Number:<br>
            <input style="width: 300px" type="text" name="phoneNumber">
            <br>
            Introduction:<br>
            <input type="text" style="width: 300px; height: 150px" maxlength="255" name="introduction">
            <br>
            <br><br><input type="submit" value="Submit" onsubmit="return check()">
        </form>
    </body>

</html>
