#include <stdio.h>
#include <string.h>
int main(int argc, char const *argv[])
{	
	char s[101];
	int n[101];
	gets(s);
	//printf("%s\n",s);
	int len=strlen(s);
	for (int i=0;i<len;i++){
		n[i]=-1;
	}
	char boy=s[0];
	char girl;
	for (int i=0;i<len;i++){
		if (s[i]!=boy){
			girl=s[i];
			break;
		}
	}
	//printf("boy=%c girl=%c\n",boy,girl);
	//printf("%d\n",len);
	for (int i=0;s[i]!='\0';i++){
		if (s[i]==girl){
			//printf("i=%d ",i);
			for (int j=i-1;j>=0;j--){
				if (s[j]==boy&& n[j]==-1){
					printf("%d %d\n",j,i);
					n[i]=i;
					n[j]=j;
					break;
				}
			}
		}
	}
	return 0;
}