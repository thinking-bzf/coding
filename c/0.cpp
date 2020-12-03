#include <stdio.h>
struct DATA
{
    int a;
    float b;
} data[2] = {1, 3.3, 3, 212.1};
int main()
{
    struct DATA *p = data;
    int a = (*(data + 1)).a;
    printf("%d", a);
    return 0;
}