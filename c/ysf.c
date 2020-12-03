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

int main(void)
{
    Time_init; //获取时钟频率

    int num, N;
    int mem[100] = {0};       //成员
    scanf("%d %d", &num, &N); //定义几个人 跳过的人数

    Time_begin; //开始计时

    int t = num; //记录自杀后的实时人数
    int i = 0;   //记录当前的位置
    while (t > 0)//n*N*
    {
        int cnt = 0;
        while (cnt < N || mem[i] == 1) //当跳过的人计数小于设定值或遇到自杀的人时跳一格
        {
            if (mem[i] == 0)
                cnt++;
            i = (i + 1) % num; //圆环用取模
        }
        //printf("%d ", i + 1); //数组和实际的序数小一，输出加一
        mem[i] = 1;
        t--;
    }
    //printf("\n");
    printf("%d\n", i + 1); //数组和实际的序数小一，输出加一
    Time_end;              //计时结束
    Time_out;              //结果                       //结果
}
