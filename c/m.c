#include<stdio.h>
#include<math.h>
int Isonciril(int x, int y, int r); 
int main(void)
{
	//画金字塔
	int width ;
	scanf("%d", &width);
	for (int a = 0; a <= width; a+=2) {
		for (int i = 0; i <= (width - a) / 2; i++) {
			printf(" ");
		}
		
		int cnt = 0;
		do {
			printf("*");
			cnt++;
		} while (cnt != a + 1);
		printf("\n");
	}
	int r ;
	scanf("%d", &r);
	for (int i = 1; i <= 2 * r + 1; i++) {
		for (int j = 1; j <= 2 * r + 1; j++) {
			if (Isonciril(i,j,r) == 0) {
				printf(" ");
			}
			else {
				printf("*");
			}
		}
		printf("\n");
	}
}
int Isonciril(int x, int y, int r)//判断是否在圆内
{
	int z = 0;
	int ison = 0;
	z = (y-r-1) * (y-r-1) + (x-r-1) * (x-r-1);
	if (abs(z-r*r)<r) {
		ison = 1;
	}
	return ison;
}

