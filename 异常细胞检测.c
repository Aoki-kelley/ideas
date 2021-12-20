#include <stdio.h>
int main(int argc, char const *argv[])
{
	int n;
	scanf("%d",&n);
	int cell[100][100]={0};
	for (int i=0;i<n;i++){
		for (int k=0;k<n;k++){
			scanf("%d",&cell[i][k]);
		}
	}
	/*for (int i=0;i<n;i++){
		for (int k=0;k<n;k++){
			printf("%d ",cell[i][k]);
		}
		printf("\n");
	}*/
	int sum=0;
	for (int i=1;i<n-1;i++){
		for (int k=1;k<n-1;k++){
			int c=cell[i][k];
			int up=cell[i-1][k];
			int down=cell[i+1][k];
			int right=cell[i][k-1];
			int left=cell[i][k+1];
			//printf("c=%d up=%d down=%d right=%d left=%d\n",c,up,down,right,left);
			if (up-c>=50 && down-c>=50 && right-c>=50 && left-c>=50){
				//printf("y\n");
				sum+=1;
			}
		}
	}
	printf("%d\n",sum);
	return 0;
}