#include <stdio.h>
int main(int argc, char const *argv[])
{
	int row,col;
	int num[100][100]={0};
	scanf("%d %d",&row,&col);
	for (int i=0;i<row;i++){
		for (int j=0;j<col;j++){
			scanf("%d",&num[i][j]);
		}
	}
	for (int i=0;i<col;i++){
		for (int j=0,a=i;a>=0 && j<row;j++,a--){
			//printf("1num[%d][%d]=%d\n",j,a,num[j][a]);
			printf("%d\n",num[j][a]);
		}
	}
	for (int i=1;i<row;i++){
		for (int j=col-1,a=i;a<row && j>=0;a++,j--){
			//printf("2num[%d][%d]=%d\n",a,j,num[a][j]);
			printf("%d\n",num[a][j]);
		}
	}
	return 0;
}