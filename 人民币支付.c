#include <stdio.h>
int main(int argc, char const *argv[])
{
	int a;
	scanf("%d",&a);
	if (a>0){
		int hun=(a-a%100)/100;
		printf("%d\n",hun);
		a-=hun*100;
		int f_ten=(a-a%50)/50;
		printf("%d\n",f_ten);
		a-=f_ten*50;
		int t_ten=(a-a%20)/20;
		printf("%d\n",t_ten);
		a-=t_ten*20;
		int ten=(a-a%10)/10;
		printf("%d\n",ten);
		a-=ten*10;
		int five=(a-a%5)/5;
		printf("%d\n",five);
		a-=five*5;
		int one=(a-a%1)/1;
		printf("%d\n",one);
		a-=one*1;
	}
	return 0;
}