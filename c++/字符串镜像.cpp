#include<iostream>
#include<stack>
#include<queue>
using namespace std;
string a;
stack<char>n;
queue<char>m;
int main()
{
	cin>>a;
	int cnt =0;
	for(int i = 0;a[i]!='&';i++){
		m.push(a[i]);
		cnt = i;
	}
	
	for(int j = cnt;a[j]!='@';j++){
		n.push(a[j]);
	}
	if(n.empty()&&m.empty()){
		cout<<"no";
		return 0;
	}
	
	for(int i = 0;i<cnt;i++){
		if((n.empty()&&!m.empty())||(!n.empty()&&m.empty())){
			cout<<"no";
			return 0;
		}
		char c = n.top();
		char d = m.front();
		if(c!=d){
			cout<<"no";
			return 0;
		}
		n.pop();
		m.pop();
	}
	cout<<cnt+1;
	
	
	return 0;
}
