#include <stdio.h>
#include <string.h>
#include <math.h>
int isletter(const char a);
int letornum(const char a);
double isnumber(const char a);//判断取到的字符是什么类型 1为A-Z或a-z 0为0-9或“.” -1为“=” -2为运算符
int num(char *a, int i, double varible[27], double *x); //对数字的处理
int main()
{
	int result = 0;
	char a[10];
	printf("Please input the expression\n");
	scanf("%s", a);
	double varible[27] = {0};//变量数组
	double lin[27] = {0};//寄存变量数组
	int s1 = 26;//第一个临时变量
	int s2 = 26;//第二个临时变量
	while (strcmp(a, "exit") != 0)
	{
		int flag1 = 1;//判断是否为赋值 初始为赋值，过等号为读写不可更改
		int flag2 = 1;//判断是否是计算
		int n = strlen(a);
		int i = 0;
		do
		{
			int m = letornum(a[i]);//判断取到的字符是什么类型 1为A-Z或a-z 0为0-9 -1为“=” -2为运算符
			if (m == 1 && flag1 == 1) //是字母且第一次出现
				s1 = isletter(a[i]);  //正在编辑的下标
			else if (m == -1)
			{			   //是等号进行下面的操作
				flag1 = -1; //进入读写状态
			}
			else if (m == 0)
			{
				if (a[i - 1] == '=')//判断是否为是赋值
					s2 = s1; //把字母下标给第二变量
				if (letornum(a[i + 1]) == 0 )//判断是否为多位数或者是否到末尾
				{ //如果是多位数进行下面的操作
					double x = 0;
					i = num(a, i, varible, &x);
					lin[s1] = x;
					i--;
				}
				else if (letornum(a[i + 1]) != 0 || i == strlen(a) - 1)
				{ //如果不是多位数或者是实数的整数部分，直接赋值
					lin[s1] = isnumber(a[i]);
				}
				if (i == strlen(a) - 1)//如果是最后一个字符的数字且不计算，直接复制给主变量
					varible[s1] = lin[s1];
			}
			else if (m == 1 && flag1 == -1)
			{
				s2 = isletter(a[i]); //第二临时变量的下标
			}
			else if (m == -2)//运算部分
			{
				i++; //将下标指向运算符之后的数字
				double x = 0;
				if (flag1 == 1 && flag2 == 1)
				{
					s2 = s1;
					flag2 = -1;
				}
				if (a[i - 1] == '+')//进行加法运算
				{
					if (letornum(a[i]) == 0)
					{
						i = num(a, i, varible, &x);
						lin[s2] = lin[s2] + x;
						i--; //将下标减一指向第一个非0的下标
					}
					else if (letornum(a[i]) == 1)
					{
						lin[s2] = lin[s2] + varible[isletter(a[i])];
					}
					if (flag2 == 1)
						varible[s1] = lin[s2];
					else if (flag2 == -1) //针对没有赋值的时候的算法
						varible[26] = lin[s2];
				}
				else if (a[i - 1] == '-')
				{ // 处理减法
					if (letornum(a[i]) == 0)
					{
						i = num(a, i, varible, &x);
						lin[s2] = lin[s2] - x;
						i--; //将下标减一指向第一个非0的下标
					}
					else if (letornum(a[i]) == 1)
					{
						lin[s2] = lin[s2] - varible[isletter(a[i])];
					}
					if (flag2 == 1)
						varible[s1] = lin[s2];
					else if (flag2 == -1)
						varible[26] = lin[s2];
				}
				else if (a[i - 1] == '*')
				{ //乘法
					if (letornum(a[i]) == 0)
					{
						i = num(a, i, varible, &x);

						lin[s2] = lin[s2] * x;
						i--; //将下标减一指向第一个非0的下标
					}
					else if (letornum(a[i]) == 1)
					{
						lin[s2] = lin[s2] * varible[isletter(a[i])];
					}
					if (flag2 == 1)
						varible[s1] = lin[s2];
					else if (flag2 == -1)
						varible[26] = lin[s2];
				}
				else if (a[i - 1] == '/')
				{ //除法
					if (letornum(a[i]) == 0)
					{
						i = num(a, i, varible, &x);
						lin[s2] = lin[s2] / x;
						i--; //将下标减一指向第一个非0的下标
					}
					else if (letornum(a[i] == 1))
					{
						lin[s2] = lin[s2] / varible[isletter(a[i])];
					}
					if (flag2 == 1)
						varible[s1] = lin[s2];
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
		if (flag1 != -1)
		{
			if (flag2 == 1)
				printf("%f\n", varible[s1]);
			else if (flag2 == -1)
				printf("%f\n", varible[26]);
		}
		printf("Please input the expression\n");
		scanf("%s1", a);
	}
	printf("over");
	getchar();
}
int letornum(const char x) //判断取到的字符是什么类型 1为A-Z或a-z 0为0-9 -1为“=” -2为运算符
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
int num(char *a, int i, double varible[27], double *x) //对数字的处理
{
	double v = 0;
	for (; letornum(a[i]) == 0 && i <= strlen(a) && a[i] != '.'; i++)
	{ //处理整数部分
		*x = *x * 10 + isnumber(a[i]);
	}
	if (a[i] == '.')
	{ //小数的解决方法
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
