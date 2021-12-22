#include <stdio.h>
int main()
{
	int n;
	int num[100]={0};
	scanf("%d",&n);
	for (int i=0;i<n;i++){
		scanf("%d",&num[i]);
	}
	for (int i=n-1;i>0;i--){
		for (int j=0;j<i;j++){
			if (num[j]>num[j+1]){
				int temp=num[j];
				num[j]=num[j+1];
				num[j+1]=temp;
			}
		}
	}
	for (int i=0;i<n;i++)
		printf("%d\n",num[i]);
	return 0;
}