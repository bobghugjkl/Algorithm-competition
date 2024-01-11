#include<iostream>
#include<stdlib.h>
#define LEN sizeof(struct Data)
using namespace std;
struct Data                                                          //����һ���ṹ��
{
 int x;
 struct Data *next;
};
int main()
{
 int n;
 struct Data *head;
 struct Data *creat(int x);                                       //������������ĺ���������ֵΪָ��
 struct Data *Move(struct Data *head);                            //����������ʵ���ƶ�
 void Print(struct Data *head);                                   //�����������������
 cin >> n;                                                        //����Ԫ�ظ�����Ҳ����scanf���
 head = creat(n);
 head = Move(head);
 Print(head);
 system("pause");                                                 //��Ϊ���ɿ���������ԭ����Ӵ���䣬ʹִ�д�����ͣ
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
  if (max <= p->x)                                             //Ѱ�����ֵ�������µ�ǰλ��        
  {
   max = p->x;
   p1 = p;                                                  //p1Ϊ���ֵ��ָ��
   p3 = p2;                                                 //p3Ϊ���ֵ��ǰһ��ָ��
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
