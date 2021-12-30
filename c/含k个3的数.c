#include <stdio.h>
#include <stdlib.h>
int main(int argc, char const *argv[])
{
	int m,k,count=0;
	int s[10];
	scanf("%d %d",&m,&k);
	if (m%19==0){
		int i=0;
		while(m!=0){
			s[i]=m%10; 
			m/=10;
			i++;
		}
		for (int j=0;j<i;j++){
			//printf("%d ",s[j]);
			if (s[j]==3){
				//printf("o\n");
				count+=1;
			}
		}
		if (count==k){
			printf("YES\n");
		}
	}
	else{
		printf("NO\n");
	}
	return 0;
}