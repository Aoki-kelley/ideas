#include <stdio.h>
int main(int argc, char const *argv[])
{
	int toatl_width,total_height;
	int img[100][100]={0};
	scanf("%d %d",&toatl_width,&total_height);
	int line,row,cro_width,cro_height;
	scanf("%d %d %d %d",&line,&row,&cro_width,&cro_height); //line-列,row-行
	for (int i=0;i<total_height;i++){
		for (int j=0;j<toatl_width;j++){
			scanf("%d",&img[i][j]);
		}
	}
	/*for (int i=0;i<total_height;i++){
		for (int j=0;j<toatl_width;j++){
			printf("%d",img[i][j]);
		}
	}*/
	for (int i=0;i<cro_height;i++){
		for (int j=0;j<cro_width;j++){
			printf("%d",img[row+i][line+j]);
			if (j!=cro_width-1){
				printf(" ");
			}
		}
		printf("\n");
	}
	return 0;
}