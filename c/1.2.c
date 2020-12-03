#include <stdio.h>
int main(void)
{
    int x = 1, y = 2;
    int s[2] = {1, &x};
    struct x
    {
        int a;
        int *p;
    };
    struct x *xx = s+1;
    printf("%d %d",xx->a,*(xx->p)++);
}