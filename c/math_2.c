#include <stdio.h>
#include <math.h>
struct xy
{
    double xave[8];
    int m;
};
int main()
{
    struct xy k[5] = {0};
    int count[5][8] = {{3, 3, 1, 6, 4},
                       {3, 5},
                       {9, 1, 1, 1, 2, 3, 1, 1},
                       {1, 2, 1, 3, 1, 3, 2},
                       {3, 1, 2, 6, 3, 5, 1, 3}};
    int sum[5] = {0};
    int cnt[5] = {0};
    double ave[5] = {0};
    double xave[5][8] = {0};
    int cnt2[5] = {29,
                   43,
                   47,
                   17,
                   22};
    int result[5] = {9, 8, 3, 4, 7};
    for (int i = 0; i < 5; i++)
        for (int j = 0; j < 8; j++)
        {
            if (count[i][j] == 0)
                break;
            sum[i] += count[i][j];
            cnt[i]++;
        }
    for (int x = 0; x < 5; x++)
    {
        ave[x] = sum[x] * 1.0 / cnt[x];
    }
    for (int i = 0; i < 5; i++)
    {
        if (cnt[i] > 3)
        {
            for (int j = 0; j < cnt[i]; j++)
            {
                xave[i][j] = fabs((sum[i] - count[i][j]) * 1.0 / (cnt[i] - 1) - ave[i]);
            }

            k[i].xave[i] = xave[i][0];
            for (int m = 0; m < cnt[i]; m++)
            {
                if (xave[i][m] > k[i].xave[i])
                {
                    k[i].xave[i] = xave[i][m];
                    k[i].m = count[i][m];
                }
            }
            ave[i] = (sum[i] - count[i][k[i].m]) * 1.0 / (cnt[i] - 1);
        }
    }
    int sum2 = 0;
    for (int x = 0; x < 5; x++)
    {
        printf("%dstar:%f\n", x + 1, ave[x]);
        sum2 += result[x] * cnt2[x];
    }
    getchar();
}
