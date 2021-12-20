#include <stdio.h>
int main(int argc, char const *argv[])
{
	char s1[40],s2[40];
	int len1,len2;
	gets(s1);
	gets(s2);
	//printf("s1=%s s2=%s\n",s1,s2);
	for (len1=0;s1[len1]!='\0';len1++)
	for (len2=0;s2[len2]!='\0';len2++)
	printf("len1=%d len2=%d",len1,len2);
	if (len1>=len2){
		for (int len2=0;s2[len2]!='\0';len2++){
			s1[len1++]=s2[len2];
			printf("%s\n",s1);
		}
		s1[len1]='\0';
		//printf("%s\n",s1);
	}
	else{
		for (len1=0;s1[len1]!='\0';len1++){
			s2[len2++]=s1[len1];
		}
		s2[len2]='\0';
		//printf("%s\n",s2);
	}
	printf("%s\n",s1);
	printf("%s\n",s2);
	return 0;
}