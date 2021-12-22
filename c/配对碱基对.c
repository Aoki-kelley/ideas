#include <stdio.h>
#include <string.h>
int main(int argc, char const *argv[])
{
	int n;
	scanf("%d",&n);
	getchar();
	char s[255];
	while(n--){
		gets(s);
		int len=strlen(s);
		for (int i=0;i<len;i++){
			switch (s[i]){
				case 'A':{
					printf("T");
					break;
				}
				case 'T':{
					printf("A");
					break;
				}
				case 'C':{
					printf("G");
					break;
				}
				case 'G':{
					printf("C");
					break;
				}
			}
		}
		printf("\n");
	}
	return 0;
}