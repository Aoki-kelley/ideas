#include <stdio.h>
#include <string.h>
int main(int argc, char const *argv[])
{
	char s[501];
	gets(s);
	int len=strlen(s);
	int sub_len=1;
	for (int i=0;i<len;i++){
		if (s[i+1]==' ' || s[i+1]=='\0'){
			//printf("i=%d,sub_len=%d\n",i,sub_len);
			if ((sub_len)%2!=0){
				int start=i-sub_len+1,end=i;
				int middle=(start+i)/2;
				//printf("start=%d,end=%d,middle=%d\n",start,end,middle);
				for (int j=0;j+start<middle;j++){
					char tmp=s[end-j];
					s[end-j]=s[start+j];
					s[start+j]=tmp;
				}
			}
			else{
				int start=i-sub_len+1,end=i;
				int middle=(start+i)/2;
				//printf("start=%d,end=%d,middle=%d\n",start,end,middle);
				for (int j=0;j+start<=middle;j++){
					char tmp=s[end-j];
					s[end-j]=s[start+j];
					s[start+j]=tmp;
				}
			}
			sub_len=0;
		}
		else{
			sub_len++;
		}
	}
	printf(s);
	return 0;
}