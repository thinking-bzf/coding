
#include<stdio.h>
#include<malloc.h>
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
typedef struct List
{
    int  data;
    struct List *next;
}LinkList;
 
 
int main()
{
    LinkList *L,*r,*s;
    L = (LinkList *)malloc(sizeof(LinkList));
    r =L;
    int n,i;
    int k;
    Time_init; //获取时钟频率
    scanf("%d%d",&n,&k);
    Time_begin; //开始计时
    for(i = 1;i<=n;i++)               ///尾插法建立循环链表
    {
        s = (LinkList *)malloc(sizeof(LinkList));
        s->data = i;
        r->next = s;
        r= s;
    }
     //n+n
    r->next =L->next;                  //让最后一个链表的下一个节点指向开头
    LinkList *p;
    p = L->next;                    
     
    while(p->next != p)                            //开始模拟（判断条件要注意：因为最后肯定剩下一个人， 所以最后一个数据的next还是他本身）
    {
        for(i = 0;i<k-1;i++)
        {
           
            p = p->next;                         //每k个数死一个人
        }
        //printf("%d ",p->next->data);
        p->next = p->next->next;                   //将该节点从链表上删除。
        p = p->next;
    }
    printf("%d\n",p->data);
    Time_end;              //计时结束
    Time_out;              //结果     
    return 0;
}
