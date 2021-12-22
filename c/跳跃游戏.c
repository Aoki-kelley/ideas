#include <stdio.h>
int main(int argc, char const *argv[])
{
	int n,times=0;
	scanf("%d",&n);
	int number[n];
	for (int j=0;j<n;j++){
		scanf("%d",&number[j]);
	}
	int i=0;
	for (;i<n;i++){
		int target=number[i];
		printf("%d %d\n",i,target);
		if (i+target<=n-1 && i+target>=0 && times<20){
			i+=target-1;
			times+=1;
			continue;
		}
		else {
			break;
		}
	}
	if (i==n-1 && times<20){
		printf("yes");
	}
	else{
		printf("no");
	}
	return 0;
}