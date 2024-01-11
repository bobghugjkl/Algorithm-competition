#include <iostream>
#include<vector>
#include<algorithm>
using namespace std;

vector<int> a;
int main()
{
    int x;

    while(cin>>x){
        if(x=='\n'){
            break;
        }
        a.push_back(x);
    }
    int max = 0 ;
   	for(int i = 0;i<a.size();i++){
   		for(int j = i+1;j<a.size();++j){
   			if(a[i]-a[j]>max){
   				max = a[i]-a[j];
			   }
		   }
	   } 
	cout<<max;
   return 0;
}


