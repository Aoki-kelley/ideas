#include <stdio.h>
int main(int argc, char const *argv[])
{
	int m,n;
	int mountain[21][21]={0};
	scanf("%d %d",&m,&n);
	for (int i=1;i<=m;i++){
		for (int j=1;j<=n;j++){
			scanf("%d",&mountain[i][j]);
		}
	}
	/*for (int i=0;i<=m+1;i++){
		for (int j=0;j<=n+1;j++){
			printf("%d ",mountain[i][j]);
		}
	}*/
	for (int i=1;i<=m;i++){
		for (int j=1;j<=n;j++){
			int current=mountain[i][j];
			int up=mountain[i-1][j];
			int down=mountain[i+1][j];
			int left=mountain[i][j-1];
			int right=mountain[i][j+1];
			if (current>=up && current>=down && current>=left && current>=right){
				printf("%d %d\n",i-1,j-1);
			}
		}
	} 
	return 0;
}