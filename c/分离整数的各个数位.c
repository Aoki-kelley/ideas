#include<stdio.h>
int main(){
	int a;
	int b[10]={0};
	scanf("%d",&a);
	int i=0;
	while(a!=0){
		b[i]=a%10; 
		a/=10;
		i++;
	}
	//printf("i=%d\n",i);
	for(int j=i-1;j>=0;j--)
		printf("%d\n",b[j]);
	return 0;
}