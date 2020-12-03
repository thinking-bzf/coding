#include <stdio.h>
void f1(int a, int b, int c, int add, int *mult)
{
    add = a + b + c;
    *mult = a * b * c;
    printf("add=%d,mult=%d\n", add, *mult);
}
int main()
{
    int x, y;
    x = y = 0;
    f1(9, 12, -4, x, &y);
    printf("add=%d,mult=%d", x, y);
    getchar();
}