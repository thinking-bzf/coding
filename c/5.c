#include <stdio.h>
#include <string.h>
int username(char* s)
{
	char *p=s;
	int flag = 0;
	int n = strlen(s);
	if ((*p >= 'A' && *p <= 'Z' || *p >= 'a' && *p <= 'z') && n >= 6 && n <= 18) {
		flag = 1;
		for (int i = 0; i < n; p++,i++) { 
			if (!(*p == '_' || *p >= 'A' && *p <= 'Z' || 
			*p >= 'a' && *p <= 'z' || *p > '0' && *p < '9'))
				flag = 0;
		}
	}
	return flag;
}
int main()
{
	char str[80];
	gets(str);
	if (username(str))
		printf("%s", str);
	else
		printf("%sERROR", str);
	getchar();
	return 0;
}