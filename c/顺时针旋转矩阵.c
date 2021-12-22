#include <stdio.h>
int main(int argc, char const *argv[])
{
	int row,col,n;
	int original_num[100][100]={0};
	int sorted_num[100][100]={0};
	scanf("%d %d %d",&row,&col,&n);
	for (int i=0;i<row;i++){
		for (int j=0;j<col;j++){
			scanf("%d",&original_num[i][j]);
		}
	}
	if (n%4==1){
		for (int i=0;i<row;i++){
			for (int j=0;j<col;j++){
				int tmp=original_num[i][j];
				sorted_num[j][row-1-i]=tmp;  //original_num[a][b]->sorted_num[b][a]
			}
		}
		for (int i=0;i<col;i++){
			for (int j=0;j<row;j++){
				printf("%d", sorted_num[i][j]);
				if (j!=row-1){
					printf(" ");
				}
			}
			printf("\n");
		}
	}
	else if (n%4==2){
		for (int i=0;i<row;i++){
			for (int j=0;j<col;j++){
				int tmp=original_num[i][j];
				sorted_num[row-1-i][col-1-j]=tmp;  //original_num[a][b]->sorted_num[a][b]
			}
		}
		for (int i=0;i<row;i++){
			for (int j=0;j<col;j++){
				printf("%d", sorted_num[i][j]);
				if (j!=col-1){
					printf(" ");
				}
			}
			printf("\n");
		}
	}
	else if (n%4==3){ //wrong
		for (int i=0;i<row;i++){
			for (int j=0;j<col;j++){
				int tmp=original_num[i][j];
				sorted_num[col-1-j][i]=tmp;  //original_num[a][b]->sorted_num[b][a]
			}
		}
		for (int i=0;i<col;i++){
			for (int j=0;j<row;j++){
				printf("%d", sorted_num[i][j]);
				if (j!=row-1){
					printf(" ");
				}
			}
			printf("\n");
		}
	}
	else if (n%4==0){
		for (int i=0;i<row;i++){
			for (int j=0;j<col;j++){
				int tmp=original_num[i][j];
				sorted_num[i][j]=tmp;  //original_num[a][b]->sorted_num[a][b]
			}
		}
		for (int i=0;i<row;i++){
			for (int j=0;j<col;j++){
				printf("%d", sorted_num[i][j]);
				if (j!=col-1){
					printf(" ");
				}
			}
			printf("\n");
		}
	}
	return 0;
}