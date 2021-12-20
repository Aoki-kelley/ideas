#include <stdio.h>
#include <string.h>
int main(void)
{
char str[101]={0};
while (gets(str) && strcmp(str,"") != 0){
        int i,flag=0,k;
        char outstr[101]={0};

        for( i=0;str[i];i++ )
        {
            if ( str[i]=='(' ) //有左括号，先置输出为$，标志增长1个
            {
                outstr[i]='$' ;
                flag++;
            }
            else if ( str[i]==')' ) //遇到右括号
            {
                if ( flag == 0 ) //没有左括号，则标为？
                    outstr[i]='?' ;
                else
                {
                    flag--; //括号数目减1
                    outstr[i]=' ' ; //当前输出为空格
                    for( k=i;k>=0;k-- ) //从当前位置向前找与之最近的左括号位置$,清为空格
                    {
                        if ( outstr[k]=='$')
                        {
                            outstr[k]=' ' ;
                            break;
                        }
                    }
                }                  
            }
            else
                outstr[i]=' ' ; //其它字符，直接输出空格
        }
        outstr[i]=0;//字符串结束符
        printf("%s\n",str);
        printf("%s\n", outstr );//输出结果
    }
    return 0;
}