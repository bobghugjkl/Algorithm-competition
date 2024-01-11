#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstring>
using namespace std;
const int N = 100010;
int n,m,mid;
int q[N];
int main()
{
	scanf("%d %d",&n,&m);
	for(int i = 0;i<n;i++){
		scanf("%d",&q[i]);
	}
	for(int i =0;i<m;i++){
		int x;
		scanf("%d",&x);
		int l =0,r=n-1;
		while(l<r){
			mid = l+r>>1;
			if(q[mid]<x)l=mid+1;
			else r = mid;
		}
		if(q[l]==x){
			printf("%d ",l);
			r=n-1;
			while(l<r){
				mid = l+r+1>>1;
				if(q[mid]>x)r = mid-1;
				else l = mid;
			}
			printf("%d\n",l);
		}else{
			printf("-1 -1\n");
		}
	}
	return 0;
 } 
