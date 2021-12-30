#include <stdio.h>
int main(int argc, char const *argv[])
{
	int a,b,c;
	scanf("%d,%d,%d",&a,&b,&c);
	if (a+b==c){
		printf("+\n");
	}
	else if (a-b==c){
		printf("-\n");
	}
	else if (a*b==c){
		printf("*\n");
	}
	else{ 
		if (b==0){
			printf("error\n");
		}
		else if (a/b==c){
			printf("/\n");
		}
		else if (a%b==c){
			printf("%%\n");
		}
		else {
			printf("error\n");
		}
	}
	return 0;
}