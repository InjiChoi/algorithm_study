#include <stdio.h>



int main(){
	
	char arr[201];
	
	gets(arr);
	
	int stack[101];
	int top = -1;
	
	for(int i=0;arr[i]!='\0';i++){
		//숫자 처리
		if(arr[i]>=48&&arr[i]<=57){
			int num = 0;
			//숫자가 일의자리 이상일 경우도 있으므로
			for(;;i++){
				if(arr[i]<48||arr[i]>57) break;
				num = num*10 + (arr[i] - 48);
			}
			top++;
			stack[top] = num;
		}
		//연산자 처리
		else{
			if(arr[i]=='+'){
				stack[top-1] = stack[top-1] + stack[top];
				top--;
			}
			else if(arr[i]=='-'){
				stack[top-1] = stack[top-1] - stack[top];
				top--;
			}
			else if(arr[i]=='*'){
				stack[top-1] = stack[top-1] * stack[top];
				top--;
			}
		}
	}
	
	printf("%d", stack[0]);
	
	return 0;
}
