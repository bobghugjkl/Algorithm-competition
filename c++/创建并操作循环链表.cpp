#include<iostream>
#include<stdlib.h>
using namespace std;
typedef struct node* LinkList;
struct node {
    int data;
    LinkList next, pre;
};
LinkList CreateLink(int n)
{
    LinkList l;
    l=(LinkList)malloc(sizeof(struct node));
    l->next = l->pre = l;
    LinkList p = l, q;
    while (n--)
    {
        q = (LinkList)malloc(sizeof(struct node));
        cin>>q->data;
        p->next = q;
        q->pre = p;
        q->next = l;
        l->pre = q;
        p = q;

    }
    return l;
}
LinkList merge(LinkList l)
{
    LinkList p = l ->next;
    int m = p->data;
    p->pre->next = p->next;
    p->next->pre = p->pre;
    free(p);
    LinkList r = l->next;
    while (r->data < m && r->next != l)
    {
        r = r->next;
    }
        if (r->next != l)
        {
            LinkList q;
            q = (LinkList)malloc(sizeof(struct node));
            q->data = m;
            q->pre = r->pre;
            q->next = r;
            r->pre->next = q;
            r->pre = q;
        }
        else {
            LinkList q;
            q = (LinkList)malloc(sizeof(struct node));
            q->data = m;
            r->next = q;
            q->pre = r;
            q->next = l;
            l->pre = q;
        }
            return l;
    }
    void show(LinkList l)
    {
        LinkList p = l->next;
        while (p != l)
        {
            cout << p->data<<" ";
            p = p->next;
        }
    }
    int main()
    {
        int n;
        LinkList L, K;
        cin >> n;
        L = CreateLink(n);
        K = merge(L);
        show(K);
        return 0;
    }



