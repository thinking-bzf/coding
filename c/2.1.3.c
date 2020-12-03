#include <stdio.h>
#include <string.h>
void c10_16(char *p, int b)
{
    int j;
    while (b > 0)
    {
        j = b % 16;
        if (j < 10)
            *p = j + 48;
        else
            *p = j + 55;
        b /= 16;
        p++;
    }
    *p = '\0';
}
int main()
{
    int a, i;
    char s[20];
    printf("Input a:\n");
    scanf("%d", &a);
    c10_16(s, a);
    for (i = strlen(s); i >= 0; i--)
        printf("%c", *(s + i));
    printf("\n");
}