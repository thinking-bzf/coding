#include <stdio.h>
#include <string.h>
#include <math.h>
int isletter(const char a);
int letornum(const char a);
double isnumber(const char a);
int num(char *a, int i, double varible[27], double *x); //处理数字的函数
int main()
{
    int result = 0;
    char a[10];
    //printf("输入表达式");
    scanf("%s", a);
    double varible[27] = {0};
    double lin[27] = {0};
    int s = 26;
    int s2 = 26; //临时变量的下标
    while (strcmp(a, "exit") != 0)
    {
        int flag = 1;  //判断是否为赋值
        int flag2 = 1; //判断是否为计算
        int n = strlen(a);
        int i = 0;

        do
        {
            int m = letornum(a[i]);
            if (m == 1 && flag == 1) //当为字母 且未进入编辑状态
                s = isletter(a[i]);  // 主变量 可编辑赋值

            else if (m == -1)
            {              //判断为等号
                flag = -1; //进入编辑状态 之后的变量只可以读
            }
            else if (m == 0)
            {
                if (a[i - 1] == '=') //等号第一个位数字 将主变量的下标赋值给只可读写变量
                    s2 = s;
                if (letornum(a[i + 1]) == 0 || i == strlen(a) - 1)
                { //开始处理数字 （多位数）
                    double x = 0;
                    i = num(a, i, varible, &x);
                    lin[s] = x;
                    i--;
                }
                else if (letornum(a[i + 1]) != 0 || i == strlen(a) - 1)
                { //如果不是多位数或者是实数的整数部分，直接赋值
                    lin[s] = isnumber(a[i]);
                }
                if (i == strlen(a) - 1)
                    varible[s] = lin[s];
            }
            else if (m == 1 && flag == -1)
            { //当为编辑状态时，出现字母 将当前字母赋值给临时变量
                if (m == 1)
                    s2 = isletter(a[i]); //第二临时变量的下标
            }
            else if (m == -2)
            {        //出现运算符
                i++; //将下标指向运算符之后的数字
                double x = 0;
                if (flag == 1 && flag2 == 1)
                { //双重判断是否为计算和赋值 并按情况改变相应状态
                    s2 = s;
                    flag2 = -1;
                }
                if (a[i - 1] == '+')
                {
                    if (letornum(a[i]) == 0)
                    { //加法
                        i = num(a, i, varible, &x);
                        lin[s2] = lin[s2] + x;
                        i--; //将下标减一指向第一个非0的下标
                    }
                    else if (letornum(a[i]) == 1)
                    {
                        lin[s2] = lin[s2] + varible[isletter(a[i])];
                    }
                    if (flag2 == 1) //针对没有赋值的时候的算法
                        varible[s] = lin[s2];
                    else if (flag2 == -1)
                        varible[26] = lin[s2];
                }
                else if (a[i - 1] == '-')
                { // 减法
                    if (letornum(a[i]) == 0)
                    {
                        i = num(a, i, varible, &x);
                        lin[s2] = lin[s2] - x;
                        i--;
                    }
                    else if (letornum(a[i]) == 1)
                    {
                        lin[s2] = lin[s2] - varible[isletter(a[i])];
                    }
                    if (flag2 == 1)
                        varible[s] = lin[s2];
                    else if (flag2 == -1)
                        varible[26] = lin[s2];
                }
                else if (a[i - 1] == '*')
                { //乘法
                    if (letornum(a[i]) == 0)
                    {
                        i = num(a, i, varible, &x);

                        lin[s2] = lin[s2] * x;
                        i--;
                    }
                    else if (letornum(a[i]) == 1)
                    {
                        lin[s2] = lin[s2] * varible[isletter(a[i])];
                    }
                    if (flag2 == 1)
                        varible[s] = lin[s2];
                    else if (flag2 == -1)
                        varible[26] = lin[s2];
                }
                else if (a[i - 1] == '/')
                { //除法
                    if (letornum(a[i]) == 0)
                    {
                        i = num(a, i, varible, &x);
                        lin[s2] = lin[s2] / x;
                        i--;
                    }
                    else if (letornum(a[i] == 1))
                    {
                        lin[s2] = lin[s2] / varible[isletter(a[i])];
                    }
                    if (flag2 == 1)
                        varible[s] = lin[s2];
                    else if (flag2 == -1)
                        varible[26] = lin[s2];
                }
            }
            i++;
        } while (i <= strlen(a));

        for (int i = 0; i <= 26; i++)
        {
            lin[i] = varible[i];
        }
        if (flag != -1)
        { //判断何时打印
            if (flag2 == 1)
                printf("%f\n", varible[s]);
            else if (flag2 == -1)
                printf("%f\n", varible[26]);
        }
        scanf("%s", a);
    }
    printf("结束");
}
int letornum(const char x)
{
    int is = 2;
    if (x >= 'A' && x <= 'Z' || x >= 'a' && x <= 'z')
        is = 1;
    else if (x >= '0' && x <= '9' || x == '.')
        is = 0;
    else if (x == '=')
        is = -1;
    else if (x == '*' || x == '/' || x == '+' || x == '-')
        is = -2;
    return is;
}
int isletter(const char x)
{
    int i = 0;
    if (x >= 'a' && x <= 'z')
        i = x - 'a';
    else if (x >= 'A' && x <= 'Z')
        i = x - 'A';
    return i;
}
double isnumber(const char x)
{
    int i = 0;
    if (x >= '0' && x <= '9')
        i = x - '0';
    return i;
}
int num(char *a, int i, double varible[27], double *x) //处理数字
{
    double v = 0;
    for (; letornum(a[i]) == 0 && i <= strlen(a) && a[i] != '.'; i++)
    { //整数部分
        *x = *x * 10 + isnumber(a[i]);
    }
    if (a[i] == '.')
    { //小数部分
        i++;
        int cnt = 0;
        for (; letornum(a[i]) == 0 && i <= strlen(a); i++)
        {
            v = v * 10 + isnumber(a[i]);
            cnt++;
        }
        for (int j = 0; j < cnt; j++)
        {
            v = v / 10.0;
        }
        *x = *x + v;
    }
    return i;
}
