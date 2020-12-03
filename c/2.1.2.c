#include <stdio.h>
#include <string.h>
int main()
{
    char s[81], *p1, *p2;
    int n;
    printf("Input a string:");
    gets(s);
    n = strlen(s);
    p1 = s;
    p2 = s+n-1;
    while (p1!=p2)
    {
        if (*p1 != *p2)
            break;
        else
        {
            p1++;
            p2--;
        }
    }
    if (p1 < p2)
        printf("NO\n");
    else
        printf("YES\n");
}