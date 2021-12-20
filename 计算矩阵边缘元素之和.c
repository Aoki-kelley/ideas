#include <stdio.h>
int main(int argc, char const *argv[])
{
	int sum;
	scanf("%d",&sum);
	int result[sum];
	for (int i=0;i<sum;i++){
		int m,n,cot=0;
		int num[100][100]={0};
		scanf("%d %d",&m,&n);
		for (int j=0;j<m;j++){
			for (int k=0;k<n;k++){
				scanf("%d",&num[j][k]);
			}
		}
		if (m==1 || n==1){
			//printf("1\n");
			for (int i=0;i<m;i++){
				for (int j=0;j<n;j++){
					//printf("%d\n",num[i][j]);
					cot+=num[i][j];
					}
				}
			}
		else{
			for (int i=0;i<n;i++){
				cot+=num[0][i]+num[m-1][i];
			}
			for (int i=0;i<m;i++){
				cot+=num[i][0]+num[i][n-1];
			}
			cot-=num[0][0]+num[m-1][0]+num[0][n-1]+num[m-1][n-1];
		}
		result[i]=cot;
		cot=0;
	}
	for (int i=0;i<sum;i++){
		printf("%d\n",result[i]);
	}
	return 0;
}