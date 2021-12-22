#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int main(int argc, char const *argv[])
{
	int a[]={3,5,7};
	char s[2];
	int n;
	while (gets(s) && strcmp(s,"") != 0){
		n=atoi(s);
		//printf("n=%d\n",n);
		int result[3]={0};
		int k=0;
		int i=0;
		while (i<3){
			if (n%a[i] == 0){
				//printf("k=%d\n",k);
				//printf("a=%d\n",a[i]);
				result[k]=a[i];
				k++;
				//printf("1\n");
			}
			//printf("i=%d",i);
			i++;
		}
		//for (int i=0;i<3;i++) printf("%d\n",result[i]);
		int s=0;
		for (int i=0;i<3;i++){
			if (result[i] != 0){
				s++;
			}
		}
		//printf("s=%d\n",s);
		if (s==0) printf("n\n");
		else{
			if (s==1) printf("%d\n",result[0]);
			if (s==2) printf("%d %d\n",result[0],result[1]);
			if (s==3) printf("%d %d %d\n",result[0],result[1],result[2]);
		}
	}
	return 0;
}