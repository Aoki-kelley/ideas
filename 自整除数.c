#include <stdio.h>
int main()
{
	int n;
	scanf("%d",&n);
	for (int i=10;i<=n;i++){
		int j=0,m=i;
		int b[100]={0};
		while(m!=0){
			b[j]=m%10;
			m/=10;
			j++;
		}
		int sum=0;
		for (int k=0;k<j;k++){
			sum+=b[k];
		}
		if (i%sum==0){
			printf("%d\n",i);
		}
	}
	return 0;
}