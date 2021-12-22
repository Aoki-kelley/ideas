#include <stdio.h>
#include <string.h>
int main(int argc, char const *argv[])
{
	char s[101];
	scanf("%s",s);
	int types=0;
	int len=strlen(s);
	for (int i=0;i<len;i++){
		if (s[i]=='(' || s[i]==')'){
			types+=1;
			break;
		}
	}
	for (int i=0;i<len;i++){
		if (s[i]=='[' || s[i]==']'){
			types+=1;
			break;
		}
	}
	for (int i=0;i<len;i++){
		if (s[i]=='{' || s[i]=='}'){
			types+=1;
			break;
		}
	}
	//printf("types=%d\n",types);
	int judge=types;
	int flag=0;
	for (int i=0;i<len;i++){
		char target=s[i];
		if (target=='('){
			flag+=1;
		}
		else if (target==')'){
			if (flag==0){
				judge-=1;
				break;
			}
			else{
                flag--;
            }
        }
    }
    flag=0;
    for (int i=0;i<len;i++){
		char target=s[i];
		if (target=='['){
			flag++;
		}
		else if (target==']'){
			if (flag==0){
				judge-=1;
				break;
			}
			else{
                flag--;
            }
        }
    }
    flag=0;
    for (int i=0;i<len;i++){
		char target=s[i];
		if (target=='{'){
			flag++;
		}
		else if (target=='}'){
			if (flag==0){
				judge-=1;
				break;
			}
			else{
                flag--;
            }
        }
    }
    if (judge != types){
    	printf("0\n");
    }
    else{
    	printf("1\n");
    }
	return 0;
}