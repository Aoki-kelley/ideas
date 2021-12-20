#include <stdio.h>
int main(int argc, char const *argv[])
{
	int num[5][5]={0};
	int n,m;
	for (int i=0;i<5;i++){
		for (int k=0;k<5;k++){
			scanf("%d",&num[i][k]);
		}
	}
	scanf("%d%d",&n,&m);
	if ((n>4 || n<0) && (m>4 || m<0)){
		printf("error\n");
	}
	else{
		int tmp[5]={0};
		for (int i=0;i<5;i++){
			tmp[i]=num[n][i];
		}
		for (int i=0;i<5;i++){
			num[n][i]=num[m][i];
			num[m][i]=tmp[i];
		}
	}
	for (int i=0;i<5;i++){
		for (int k=0;k<5;k++){
			printf("%4d",num[i][k]);
		}
		printf("\n");
	}
	return 0;
}