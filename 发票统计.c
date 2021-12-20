#include <stdio.h>
int main(int argc, char const *argv[])
{
	int p_id;
	char b_type[3]={'A','B','C'};
	float p_money[3]={0,0,0};  //1,2,3
	float bill_money[3]={0,0,0};  //A,B,C
	for (int i=0;i<3;i++){
		scanf("%d",&p_id);
		//printf("p_id=%d\n",p_id);
		getchar();
		int bill_sum=0;
		scanf("%d",&bill_sum);
		//printf("bill_sum=%d\n",bill_sum);
		getchar();
		for (int i=0;i<bill_sum;i++){
			char bill_type;
			float money;
			scanf(" %c %f",&bill_type,&money);
			//printf("%c %.2f\n",bill_type,money);
			p_money[p_id-1]+=money;
			switch (bill_type){
				case 'A':bill_money[0]+=money;break;
				case 'B':bill_money[1]+=money;break;
				case 'C':bill_money[2]+=money;break;
			}
		}
		getchar(); //读走换行符
	}
	for (int i=0;i<3;i++) {printf("%d %.2f\n",i+1,p_money[i]);}
	for (int i=0;i<3;i++) {printf("%c %.2f\n",b_type[i],bill_money[i]);}
	return 0;
}