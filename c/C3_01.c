#include<stdio.h>
#include<string.h>
struct student
{
	int id;
	char name[12];
	struct student* next;
};
int main()
{
	struct student a;
	a.id = 10;
	strcpy(a.name, "FangRuiXin");
	a.next = &a;
	struct student* p= &a ;
	struct student* pa =&a ;
	struct student* pStudent = &a;
	printf("%d\n", (*p));
	printf("%s\n", ((char*)(pa)+sizeof(int)));
	printf("%x\n", pStudent);
	printf("%p", &a);
	getchar();
}
