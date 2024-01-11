/*
 假设一算术表达式中包括三种括号：圆括号&ldquo;（&rdquo;和&ldquo;）&rdquo;，方括号&ldquo;[&rdquo;和&ldquo;]&rdquo;，
 花括号&ldquo;{&rdquo;和&ldquo;}&rdquo;，
 且三种括号可按意次序嵌套使用，
 试编写程序判定输入的表达式所含的括号是否正确配对出现。
 若匹配，则返回1，否则返回0。
*/
#include<iostream>
#include<stack>
#include<cstring>
using namespace std;
stack<char>s;
string c;
int main(){
	cin>>c;
	for(int i =0;i<c.length();i++){
		if(c[i]=='('||c[i]=='['||c[i]=='{'){
			s.push(c[i]);
		}
		if(c[i]==')'||c[i]==']'||c[i]=='}'){
			if(s.empty()){
				cout<<"0";
				return 0;
			}
			char a = s.top();
			s.pop();
			if((a!='('&&c[i]==')')||(a!='['&&c[i]==']')||(a!='{'&&c[i]=='}')){
				cout<<"0";
				return 0;
			}
		}
	}
	if(s.empty()){
		cout<<"1";
		
	}else{
		cout<<"0";
	}
	return 0;
}
