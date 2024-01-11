#include <iostream>
#include<vector>
using namespace std;
vector<char>a;
int main()
{
    char b;
    while(cin>>b){
        if(b=='#'){
            break;
        }
        a.push_back(b);
    }
    for(int i = 0;i<a.size();i++){
            if(i%2==0){
                cout<<a[i];
            }

    }
    for(int j = a.size()-1;j>=0;j--){
        if(j%2!=0){
            cout<<a[j];
        }
    }

    return 0;
}


