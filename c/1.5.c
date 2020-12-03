#include <stdio.h>
int main()
{
    int i = 3, *pi, **ppi;
    pi = &i;
    ppi = &pi;
    printf("i=%d,*pi=%d,**ppi=%d\n", i, *pi, **ppi);
    i++;
    printf("i=%d,*pi=%d,**ppi=%d\n", i, *pi, **ppi);
    getchar();
}