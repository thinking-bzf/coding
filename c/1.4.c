#include <stdio.h>
#define SIZE 12
void sub(char *a, int t1, int t2)
{
    char ch;
    while (t1 < t2)
    {
        ch = *(a + t1);
        *(a + t1) = *(a + t2);
        *(a + t2) = ch;
        t1++;
        t2--;
    }
}
int main()
{
    char s[SIZE];
    int i;
    for (i = 0; i < SIZE; i++)
        s[i] = 'A' + i + 32;
    sub(s, 7, SIZE - 1);
    for (i = 0; i < SIZE; i++)
        printf("%c", s[i]);
    printf("\n");
    getchar();
}