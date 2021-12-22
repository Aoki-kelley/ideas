#include <stdio.h>
int main(int argc, char const *argv[])
{
	int year;
	scanf("%d",&year);
	if (year%400==0 || (year%4==0 && year%100!=0)){
		printf("Y\n");
	}
	else{
		printf("N\n");
	}
	return 0;
}