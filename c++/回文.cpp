#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
int main() {
	string a;
	cin >> a;
	string b = a;
	reverse(b.begin(), b.end());//反转字符串
	if (a == b) cout << a << "是回文串" << endl;
	else cout << a << "不是回文串" << endl;
	return 0;
}

