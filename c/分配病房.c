#include<stdio.h>
#include<stdlib.h>
#include<string.h>
struct Person{
		char no[4]; //编号 
		double num;//严重程度 
	};
int cmp(const void *a,const void *b){
	return *(int *)b-*(int *)a;
}
int main(){
	int n;
	double a;
	struct Person group[50];
	struct Person group2[50]; //用来保存新的结构数据（重症病房的） 
	scanf("%d%lf\n",&n,&a);
	int i,j=0,t;
	char T[10];
	double temp=0;
	for(i=0;i<n;i++){
		scanf("%s%lf", &group[i].no, &group[i].num);
	}
	for(i=0;i<n;i++){
		if(group[i].num>=a){
			strcpy(group2[j].no, group[i].no);
			group2[j].num=group[i].num;
			j++;
	}
	}
	if(j==0)
		printf("None.");
	else{
//		qsort(group2.num,j,sizeof(group2[0].num),cmp); qsort不能对结构里的数组使用吗？
		for(i=0;i<j-1;i++){
			for(t=0;t<j-i;t++){
				if(group2[t].num<group2[t+1].num){
				temp=group2[t].num;
				group2[t].num=group2[t+1].num;
				group2[t+1].num=temp;
				strcpy(T,group2[t].no);
				strcpy(group2[t].no,group2[t+1].no);
				strcpy(group2[t+1].no,T);    //rcpy可以操作结构内元素，这里是机智但是很麻烦地把冒泡排序应用到了交换两个字符串中 
				}
			}
		}
		for(i=0;i<j;i++){
			printf("%s %.1f\n",group2[i].no,group2[i].num);
		}
	}
	
}