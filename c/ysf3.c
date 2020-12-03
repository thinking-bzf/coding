
#include <stdio.h>
#include <math.h>
#include <windows.h> //头文件
#define Time_init             \
    LARGE_INTEGER lFrequency; \
    QueryPerformanceFrequency(&lFrequency);
#define Time_begin             \
    LARGE_INTEGER lBeginCount; \
    QueryPerformanceCounter(&lBeginCount);
#define Time_end             \
    LARGE_INTEGER lEndCount; \
    QueryPerformanceCounter(&lEndCount);
#define Time_out                                                                                     \
    double time = (double)(lEndCount.QuadPart - lBeginCount.QuadPart) / (double)lFrequency.QuadPart; \
    printf("run:%lfms\n", time * 1000);
int main()
{
    int n, m, i, s = 0;
    Time_init; //获取时钟频率
    scanf("%d%d", &n, &m);
    Time_begin; //开始计时
    for (i = 2; i <= n; i++)
        s = (s + m + 1) % i;
    printf("%d\n", s + 1);
    Time_end; //计时结束
    Time_out; //结果
    return 0;
}
