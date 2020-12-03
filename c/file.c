#include <stdio.h>
#include <math.h>
#include <windows.h>
int main(void)
{

    double f, z, y, x;
    int i = 2.0 / 3;
    for (y = 25; y > -20; y -= 1)
    {
        for (x = -20; x < 20; x += 0.5)
        {
            f = x * x + (y - pow(x * x, 1.0 / 3)) * (y - pow(x * x, 1.0 / 3));
            f -= 400;
            if (f < 0.0)
            {
                printf("*");
            }
            else
            {
                printf(" ");
            }
        }
        Sleep(100);
        printf("\n");
    }
    
    getchar();
}