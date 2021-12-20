#include <stdio.h>
int main(int argc, char const *argv[])
{
	int n=-1;
	int num[500]={0};
	while (n != 0){
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
		/*for (int i=0;i<n;i++)
			printf("%d\n",num[i]);*/
		int index=n/2;
		if (n%2==0 && n>0){
			int result=(num[index-1]+num[index])/2;
			printf("%d\n",result);
		}
		else if (n%2==1 && n>0){
			int result=num[index];
			printf("%d\n",result);
		}
	}
	return 0;
}