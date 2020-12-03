<%@ page language="java" import ="java.util.*" contentType="text/html;charset=utf-8"%>

<% 
    Date dnow = new Date();
    int dhours = dnow.getHours();
    int dweek = dnow.getDay();
    int dminutes = dnow.getMinutes();
    String noon = "上午";
    String week = "星期一";
    if(dhours == 12)
        {noon = "中午";}
    else if(dhours < 12)
        {noon = "上午";}
    else if(dhours > 12)
        {noon = "下午";}
    
    if(dweek == 0)  week = "星期日";
    if(dweek == 1)  week = "星期一";
    if(dweek == 2)  week = "星期二";
    if(dweek == 3)  week = "星期三";
    if(dweek == 4)  week = "星期四";
    if(dweek == 5)  week = "星期五";
    if(dweek == 6)  week = "星期六";
    out.print("<p>今天是" + week +","+ noon + dhours + "点" + dminutes + "分</p>");
%>
</script>
