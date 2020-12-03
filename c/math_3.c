#include <stdio.h>
#include <math.h>
struct ration
{
    int num;
    double hour;
    int c;
};
int main()
{
    struct ration xy[3] = {0, 0, 0};
    double t[3] = {83.07 / 60, 75.60 / 60, 71.11 / 60};
    int m[3] = {9, 9, 5};
    double x[3] = {0};
    for (int i = 0; i < 3; i++)
    {
        double min = 0.2;
        for (int n = 1; n <= m[i]; n++)
        {
            int q = 0;
            if (m[i] % n != 0)
                q = ceil(m[i] * 1.0 / n);
            else
                q = floor(m[i] * 1.0 / n);
            double h = t[i] * ceil(m[i] * 1.0 / n) * 1.1;
            x[i] = (h * n * n) / (m[i] * m[i]);
            if (min > fabs(x[i] - 0.7) && q > 1)
            {
                xy[i].num = n;
                xy[i].hour = h;
                xy[i].c = q;
            }
        }
    }
    for (int j = 0; j < 3; j++)
        printf("n=%d,h[%d]=%.2f,c[%d]=%d\n", xy[j].num, j, xy[j].hour, j, xy[j].c);
    getchar();
}