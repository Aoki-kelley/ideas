#include <stdio.h>
int main(int argc, char const *argv[])
{
	int n,m;
	char room[100][100];
	scanf("%d",&n);
	for (int i=1;i<n+1;i++){
		for (int j=1;j<n+1;j++){
			scanf("%c",&room[i][j]);
			if (room[i][j]=='\n') scanf("%c",&room[i][j]);
		}
	}
	scanf("%d",&m);
	while (m>0){
		for (int i=1;i<n+1;i++){
			for (int j=1;j<n+1;j++){
				if (room[i][j]=='@'){
					if (room[i][j-1]=='.') room[i][j-1]='!';
					if (room[i][j+1]=='.') room[i][j+1]='!';
					if (room[i-1][j]=='.') room[i-1][j]='!';
					if (room[i+1][j]=='.') room[i+1][j]='!';
				}
			}
		}
		m-=1;
		if (m>0){
			for (int i=1;i<n+1;i++){
				for (int j=1;j<n+1;j++){
					if (room[i][j]=='!') room[i][j]='@';
				}
			}
		}
	}
	int sum=0;
	for (int i=1;i<n+1;i++){
		for (int j=1;j<n+1;j++){
			//printf("%c",room[i][j]);
			if (room[i][j]=='@') sum+=1;
		}
		//printf("\n");
	}
	printf("%d\n",sum);
	return 0;
}