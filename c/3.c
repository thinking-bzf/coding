#include <stdio.h>
#include <string.h>
void mystr(char a[], char b[], int m)
{
    int *p=a;
    for (int i = 0; i < m; i++)
        a++;
    for (; *b != '\0'; b++)
    {
        *a = *b;
        a++;
    }
    *a='\0';
    a=p;
    printf("%s",a);
}
int main()
{
    int n, m;
    char a[10], b[10];
    printf("Input a:\n");
    scanf("%s", a);
    printf("Input the site");
    scanf("%d", &m);
    printf("Input b:\n");
    scanf("%s", b);
    mystr(a, b, m);
}