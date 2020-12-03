#include <stdio.h>
#include <string.h>
int main()
{
    int c[32] = {0};
    char a[32] = "abcdefghijklmnopqrstuvwxyz123456";
    char b[32] = "cinbjloagekhdpmfsy4rz25qwu1xt63v";
    for (int i = 0; i < 32; i++)
    {
        for (int j = 0; j < 32; j++)
        {
            if (a[i] == b[j])

                c[i] = j;
        }
    }
    char d[32] = "a$mgt5phje+UmLI{PA!_T0!3uRiTe}nm";
    char e[32];
    for (int i = 0; i < 32; i++)
    {
        e[i] = d[c[i]];
    }
    printf("%s", e);
}