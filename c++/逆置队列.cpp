#include<iostream>
#include<queue>
#include<stack>
using namespace std;
queue<int>a;
stack<int>b;
int main(){
	int n;
	cin>>n;
	while(n--){
		int m;
		cin>>m;
		b.push(m);
	}
	while(!b.empty()){
		cout<<b.top()<<" ";
		b.pop();
	}
	return 0;
} 
