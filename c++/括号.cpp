/*
 ����һ�������ʽ�а����������ţ�Բ����&ldquo;��&rdquo;��&ldquo;��&rdquo;��������&ldquo;[&rdquo;��&ldquo;]&rdquo;��
 ������&ldquo;{&rdquo;��&ldquo;}&rdquo;��
 ���������ſɰ������Ƕ��ʹ�ã�
 �Ա�д�����ж�����ı��ʽ�����������Ƿ���ȷ��Գ��֡�
 ��ƥ�䣬�򷵻�1�����򷵻�0��
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
