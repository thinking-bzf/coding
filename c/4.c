#include <stdio.h>
#include <string.h>
void mypx(char *x[5])
{
	char* t;
	for (int i = 0; i < 4; i++) {
		int k = i;
		for (int j = i + 1; j < 5; j++) 
			if (strcmp(x[j], x[k]) < 0)
				k = j;
		t = x[k];
		x[k] = x[i];
		x[i] = t;
	}
	for (int i = 0; i < 5; i++)
		printf("%s\n", x[i]);
}
int main()
{
	char *str[5];
	for (int i = 0; i < 5; i++)
	{
		char m[5][10];
		scanf("%s", m[i]);
		str[i] = m[i];
	}
	printf("\n");
	mypx(str);
	
}