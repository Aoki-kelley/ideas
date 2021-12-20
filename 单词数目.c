#include <stdio.h>
int main(int argc, char const *argv[])
{
	char s[50];
	int flag=0,num=0;
	gets(s);
	for (int i=0;s[i]!='\0';i++){
		if (s[i]==' '){
			flag=0;
		}
		else if(flag==0){
			flag=1;
			num++;
		}
	}
	printf("%d\n",num);
	return 0;
}