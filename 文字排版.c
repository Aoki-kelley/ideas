#include <stdio.h>
#include <string.h>
int main(int argc, char const *argv[])
{
	char s[1000];
	int num=0;
	scanf("%d",&num);
	getchar();
	gets(s);
	int slen=strlen(s);
	int len=0,sub_len=0;
	//printf("%d\n",slen);
	for (int i=0;i<slen;i++){
		if (s[i]!=' '){
			printf("%c",s[i]);
			len++;
		}
		else {
			for (int j=i+1;j<slen;j++){
				if (s[j]!=' '){
					sub_len++;
				}
				else {
					break;
				}
			}
			//printf("|sub_len=%d,len=%d|",sub_len,len);
			if (len+sub_len<80){
				printf("%c",s[i]);
				sub_len=0;
				len++;
			}
			else {
				printf("\n");
				sub_len=0;
				len=0;
			}
		}
	}
	return 0;
}