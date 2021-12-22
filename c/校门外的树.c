#include <stdio.h>
int main(int argc, char const *argv[])
{
	int L,M;
	int zone[100][2],t[10000]={0};
	scanf("%d%d",&L,&M);
	for (int i=0;i<L+1;i++){
		t[i]=1;
	}
	for (int i=0;i<M;i++){
		scanf("%d%d",&zone[i][0],&zone[i][1]);
	}
	int a,b;
	for (int i=0;i<M;i++){
		a=zone[i][0];
		b=zone[i][1];
		for (int k=a;k<b+1;k++){
			if (t[k]==1) t[k]=0;
		}
	}
	int sum=0;
	for (int i=0;i<L+1;i++){
		if (t[i]==1) sum+=1;
	}
	printf("%d\n",sum);
	return 0;
}