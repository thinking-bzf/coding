#include <stdio.h>
#include <string.h>
int main()
{
	char passwd[] = "y0uZh1yu4n";
	char key[] = "helloworld";
	char part1[11];
	char part2[11];
	for (int i = 0; i < strlen(passwd); i++) {
		part1[i] = (passwd[i] & 0x55) | (key[i] & 0xaa);
		part2[i] = (passwd[i] & 0xaa) | (key[i] & 0x55);
		printf("%02x", ((part2[i] & 0xf) << 4) | (part1[i] & 0xf));
		printf("%02x", (part2[i] & 0xf0) | ((part1[i] & 0xf0) >> 4));
	}
	
	
	
	printf("\n");
	char in[41] = "896750634d67e847da665373db6707774c63e466";
	int pw[40] = { 0 };
	int i = 0;
	for ( i = 0; i < 40; i++) {                              
		if (in[i] >= '0' && in[i] <= '9')
			pw[i] = in[i] - '0';
		if (!(in[i] >= '0' && in[i] <= '9'))
			pw[i] = in[i] - 'a' + 10;
	}
	int j = 0;
	for ( j = 0; j < 10;j++) {
		int p2[2] = { pw[4 * j + 2] ,pw[4 * j] };
		int p1[2] = { pw[4 * j + 3] ,pw[4 * j + 1] };
		int password1 = p2[0] << 4 & 0xaa | (p2[1] & 0xaa);
		int password2 = p1[0] << 4 & 0x55 | (p1[1] & 0x55);
		printf("%c", password1 | password2);
	}
	getchar();
}


