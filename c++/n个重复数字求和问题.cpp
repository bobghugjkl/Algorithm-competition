#include <iostream>

using namespace std;

int main()
{
    int a,n;
    cin>>a>>n;
    int sum=0;
    for(int i = 1;i<=n;i++){
            int b=a;
        for(int j = 1;j<i;j++){
            b*=10;
            b+=a;

        }

    sum+=b;
    }
    cout<<sum;
    return 0;
}


