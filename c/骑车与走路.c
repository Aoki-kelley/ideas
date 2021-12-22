#include <stdio.h>
int main()
{
	int n,m;
	int num[100]={0};
	scanf("%d",&n);
	for (int i=0;i<n;i++){
		scanf("%d",&num[i]);
	}
	for (int i=0;i<n;i++){
		float time1,time2; //骑行，步行
		m=num[i];
		time1=50.0+m/3.0;
		time2=m/1.2;
		//printf("time1=%f,time2=%f",time1,time2);
		if (time1<time2)
			printf("Bike\n");
		else{
			if (time1==time2)
				printf("All\n");
			else
				printf("Walk\n");
		}
	}
	return 0;
}