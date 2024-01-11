#include<iostream>
#include<algorithm>
#include<cstdio>
#include<string>
using namespace std;
int f(int n)
{
    if(n<8)
    {

        return n;
    }else{
        return n%8+10*f(n/8);
    }

}
int main()
{
    int n;
    cin>>n;
    cout<<f(n);
    return 0;

}

