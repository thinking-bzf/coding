#include<stdio.h>
#include<string.h>
int N=3;
void multiple_matrix(int ** ,int ** ,int );
int input(int ** ,int);
int output(int * ,int);
int main()
{
	int A[3][3],B[3][3];
	int i;
	int *pa[3],*pb[3];
	for(i=0;i<3;i++)
	{
		pa[i]=A[i];
		pb[i]=B[i];
	}
	int **pA=pa,**pB=pb;
	input(A,N);
	multiple_matrix(pA,pB,N);
	output(*B,N);
} 

int input(int **p,int N)//输入3*3矩阵 
{
	int i,j;
	printf("请输入3*3的矩阵：\n");
	for(i=0;i<N;i++)
	{
		for(j=0;j<N;j++)
		{
			scanf("%d",*(p+i)+j);
		}
	}
}

void multiple_matrix(int **MatrixA,int **MatrixB,int N)//计算 
{
	int i,j,k;
	for(i=0;i<N;i++)
	{
		for(j=0;j<N;j++)
		{
			for(k=0;k<N;k++)
			{
				*(*(MatrixB+i)+j)=*(*(MatrixA+i)+k)**(*(MatrixA+k)+j);
			}
		}
	}
}

int output(int *x,int N)//输出 
{
	int i,j;
	for(i=0;i<N;i++)
	{
		for(j=0;j<N;j++)
		{
			printf("B=A*A=%d\n",*(x+i)+j);
		}
	}
}