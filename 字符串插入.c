//一次输入多行后处理
/*#include <stdio.h>
#include <string.h>
int main(int argc, char const *argv[])
{
	char s[20];
	char data[20][20];
	char str[16];
	char substr[4];
	int i=0;
	while (gets(s) && strcmp(s,"") != 0){
		int len=strlen(s);
		//printf("s=%s len=%d\n",s,len);
		for (int j=0;j<len;j++){
			data[i][j]=s[j];
			//printf("1\n");
		}
		i++;
	}
	//printf("i=%d\n",i);
	//for (int i1=0;i1<i;i1++){
		//printf("%s\n",data[i1]);
	//}
	for (int i2=0;i2<i;i2++){
		strcpy(s,data[i2]);
		int i3=0;
		for (i3=0;s[i3]!=' ';i3++){
			str[i3]=s[i3];
		}
		str[i3]='\0';
		int k=0;
		int len=strlen(s);
		for (i3=i3+1,k=0;i3<len+1;i3++,k++){
			substr[k]=s[i3];
		}
		//printf("str=%s substr=%s\n",str,substr);
		int m=0;
		for (int j=0;str[j]!='\0';j++){
			if (str[j]>str[m]){
				m=j;
			}
		}
		//printf("m=%d\n",m);
		int len1=strlen(str);
		char tmp[10];
		for (int i=m+1,k=0;i<len1+1;i++,k++){
			tmp[k]=str[i];
		}
		//printf("tmp=%s len=%d\n",tmp,strlen(tmp));
		int len2=strlen(substr);
		for (int i=m+1,k=0;k<len2+1;i++,k++){
			str[i]=substr[k];
		}
		len1=strlen(str);
		int len3=strlen(tmp);
		//printf("str=%s len=%d\n",str,len1);
		for (int i=len1,k=0;k<len3+1;i++,k++){
			str[i]=tmp[k];
		}
		printf("%s\n",str);
	}
	return 0;
}*/
//每输入一行处理
#include <stdio.h>
#include <string.h>
int main(int argc, char const *argv[])
{
    char s[20];
    char str[16];
    char substr[4];
    while (gets(s) && strcmp(s,"") != 0){
        int len=strlen(s);
        //printf("s=%s len=%d\n",s,len);
        int i3=0;
        for (i3=0;s[i3]!=' ';i3++){
            str[i3]=s[i3];
        }
        str[i3]='\0';
        int k=0;
        //int len=strlen(s);
        for (i3=i3+1,k=0;i3<len+1;i3++,k++){
            substr[k]=s[i3];
        }
        //printf("str=%s substr=%s\n",str,substr);
        int m=0;
        for (int j=0;str[j]!='\0';j++){
            if (str[j]>str[m]){
                m=j;
            }
        }
        //printf("m=%d\n",m);
        int len1=strlen(str);
        char tmp[10];
        for (int i=m+1,k=0;i<len1+1;i++,k++){
            tmp[k]=str[i];
        }
        //printf("tmp=%s len=%d\n",tmp,strlen(tmp));
        int len2=strlen(substr);
        for (int i=m+1,k=0;k<len2+1;i++,k++){
            str[i]=substr[k];
        }
        len1=strlen(str);
        int len3=strlen(tmp);
        //printf("str=%s len=%d\n",str,len1);
        for (int i=len1,k=0;k<len3+1;i++,k++){
            str[i]=tmp[k];
        }
        printf("%s\n",str);
    }
    return 0;
}