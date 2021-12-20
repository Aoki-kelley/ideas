#include <stdio.h>
int f(int x){
	if (x==1){
		printf("End\n");
		return 0;
	}
	if (x%2==0){
		int y=x/2;
		printf("%d/2=%d\n",x,y);
		return f(y);
	}
	else{
		int y=x*3+1;
		printf("%d*3+1=%d\n",x,y);
		return f(y);
	}
}
int main(int argc, char const *argv[])
{
	int n;
	scanf("%d",&n);
	f(n);
	return 0;
}