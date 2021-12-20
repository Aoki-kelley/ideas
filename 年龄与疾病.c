#include <stdio.h>
int main()
{
	float n;
	int age[100]={0};
	int duan[100]={0};
	scanf("%f",&n);
	for (int i=0;i<n;i++)
		scanf("%d",&age[i]);
	for (int i=0;i<n;i++){
		int a=age[i];
		if (a<19)
			duan[0]+=1;
		if (19<=a && a<36)
			duan[1]+=1;
		if (36<=a && a<61)
			duan[2]+=1;
		if (61<=a)
			duan[3]+=1;
	}
	printf("1-18: %.2f%%\n",duan[0]/n*100);
	printf("19-35: %.2f%%\n",duan[1]/n*100);
	printf("36-60: %.2f%%\n",duan[2]/n*100);
	printf("61-: %.2f%%\n",duan[3]/n*100);
	return 0;
}