#include<iostream>
#include<stdlib.h>
#define LEN sizeof(struct Data)
using namespace std;
struct Data                                                          //定义一个结构体
{
 int x;
 struct Data *next;
};
int main()
{
 int n;
 struct Data *head;
 struct Data *creat(int x);                                       //声明建立链表的函数，返回值为指针
 struct Data *Move(struct Data *head);                            //声明函数，实现移动
 void Print(struct Data *head);                                   //函数声明，输出链表
 cin >> n;                                                        //输入元素个数，也可用scanf语句
 head = creat(n);
 head = Move(head);
 Print(head);
 system("pause");                                                 //因为集成开发环境的原因，添加此语句，使执行窗口暂停
 return 0;
}
struct Data *creat(int x)
{
 struct Data *head, *p1, *p2;
 int n;
 head = (struct Data *)malloc(LEN);
 head->x = x;
 p1 = p2 = (struct Data *)malloc(LEN);
 for (n = 1; n <= x; n++)
 {
  cin >> p1->x;
  if (n == 1)
   head->next = p1;
  else
   p2->next = p1;
  p2 = p1;
  p1 = (struct Data *)malloc(LEN);
 }
 p2->next = NULL;
 free(p1);
 return head;
}
void Print(struct Data *head)
{
 struct Data *p;
 for (p = head->next; p != NULL; p = p->next)
 {
  cout << p->x << " ";
 }
 cout << endl;
}
struct Data *Move(struct Data *head)
{
 struct Data *p, *p1, *p2, *p3;
 int max;
 max = head->next->x;
 p = p1 = p2 = p3 = NULL;
 for (p = head->next, p2 = head; p != NULL; p = p->next, p2 = p2->next)
 {
  if (max <= p->x)                                             //寻找最大值，并记下当前位置        
  {
   max = p->x;
   p1 = p;                                                  //p1为最大值的指针
   p3 = p2;                                                 //p3为最大值的前一个指针
  }
 }
 if (p1->next != NULL)
 {
  p3->next = p1->next;
  p2->next = p1;
  p1->next = NULL;
 }
 else
  p1->next = NULL;
 return head;
}
