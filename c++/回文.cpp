#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
int main() {
	string a;
	cin >> a;
	string b = a;
	reverse(b.begin(), b.end());//��ת�ַ���
	if (a == b) cout << a << "�ǻ��Ĵ�" << endl;
	else cout << a << "���ǻ��Ĵ�" << endl;
	return 0;
}

