#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cmath>
#include<cstring> 
using namespace std;
class Sort
{
	public:
		Sort(int r[],int n);
		~Sort();
		void InsertSort();
		void NewInsertSort();
		void ShellSort();
		void BubbleSort();
		void QuickSort(int first,int last);
		void SelectSort();
		void HeapSort();
		void Print();
		
		
	private:
		int Partition(int first,int last);
		void Sift(int k,int last);
		int *data;
		int length;
};
Sort::Sort(int r[],int n)
{
	data = new int[n];
	for(int i = 0;i < n;i++)
	{
		data[i] = r[i];
	}
	length = n;
}
Sort::~Sort()
{
	delete[]data;
}
void Sort::Print()
{
	for(int i = 0;i<length;i++)
	{
		cout<<data[i]<<"\t";
	}
	cout<<endl;
}
//直接插入排序
void Sort::InsertSort()
{
	int i,j,temp;
	for(i = 1;i<length;i++)
	{
		temp = data[i];
		for(j = i-1;j>=0&&temp<data[j];j--)
		{
			data[j+1] = data[j];	
		}
		data[j+1]=temp;	
	}	
} 
//折半优化 
void Sort::NewInsertSort()
{
	for (int i = 1; i < length; i++)  
    {  
        int temp = data[i];  
        int left = 0;  
        int right = i - 1;  
        int mid;  
  
        // 使用二分搜索找到插入位置  
        while (left <= right)  
        {  
            mid = left + (right - left) / 2;  
            if (temp <= data[mid])  
                right = mid - 1;  
            else  
                left = mid + 1;  
        }  
  
        // 将元素后移并插入  
        for (int j = i - 1; j >= left; j--)  
        {  
            data[j + 1] = data[j];  
        }  
        data[left] = temp;  
    }  
}
//希尔排序
void Sort::ShellSort()
{
	int d,i,j,temp;
	for(d = length/2;d>=1;d=d/2)
	{
		for(i = d;i<length;i++)
		{
			temp = data[i];
			for(j = i - d;j>=0&&temp<data[j];j=j-d)
			{
				data[j+d] = data[j];	
			}
			data[j+d] = temp;	
		}	
	}	
} 
//起泡排序
void Sort::BubbleSort()
{
	int j,exchange,bound,temp;
	exchange = length - 1;
	while(exchange != 0)
	{
		bound = exchange;exchange = 0;
		for(j = 0;j<bound;j++)
		{
			if(data[j]>data[j+1])
			{
				temp = data[j];data[j] = data[j+1];data[j+1] = temp;
				exchange = j;	
			}	
		}	
	}	
} 
int Sort::Partition(int first,int last)
{
	int i = first,j = last,temp;
	while(i<j)
	{
		while(i<j&&data[i]<=data[j])j--;
		if(i<j){
			temp = data[i];data[i] = data[j];data[j] = temp;
			i++;
		}
		while(i<j&&data[i]<=data[j])i++;
		if(i<j){
			temp = data[i];data[i] = data[j];data[j] = temp;
			j--;
		}
	}
	return i;
}
void Sort::QuickSort(int first,int last)
{
	if(first >= last)
	{
		return;
	}
	else{
		int pivot = Partition(first,last);
		QuickSort(first,pivot-1);
		QuickSort(pivot+1,last);
	}
}
void Sort::SelectSort()
{
	int i,j,index,temp;
	for(i = 0;i<length-1;i++)
	{
		index = i;
		for(j = i+1;j<length;j++)
		{
			if(data[j]<data[index]){
				index = j;
			}
		}
		if(index!=i)
		{
			temp = data[i];
			data[i] = data[index];
			data[index] = temp;
		}
	}
}
void Sort::Sift(int k,int last)
{
	int i,j,temp;
	i = k,j = 2*i+1;
	while(j<=last){
		if(j<last&&data[j]<data[j+1])j++;
		if(data[i]>data[j])break;
		else{
			temp = data[i];data[i] = data[j];data[j] = temp;
			i = j;j = 2*i+1;
		}
	}
}
void Sort::HeapSort()
{
	int i,temp;
	for(i = ceil(length/2)-1;i>=0;i--)
	{
		Sift(i,length-1);
	}
	for(i = 1;i<length;i++)
	{
		temp = data[0];data[0] = data[length-i];data[length-i] = temp;
		Sift(0,length-i-1);
	} 
}
int main()
{
	int select,r[10] = {2,5,1,7,9,4,3,6,5,8};
	Sort L{r,10};
	cout<<"1.直接插入排序，2.希尔排序，3.起泡排序，4.快速排序，5.简单选择排序，6.堆排序";
	cout<<endl;
	cout<<"请输入要使用的技术编号:";
	cin>>select;
	switch(select)
	{
		case 1:L.InsertSort();break;
		case 2:L.ShellSort();break;
		case 3:L.BubbleSort();break;
		case 4:L.QuickSort(0,9);break;
		case 5:L.SelectSort();break;
		case 6:L.HeapSort();break;
		default:cout<<"输入编号错误"<<endl;break;	
	}
	
	L.Print();
	return 0;	
} 
