#include<bits/stdc++.h>
using namespace std;

typedef struct Node {//����ڵ� 
	int num;
	struct Node *next;
} Lnode,*LinkList;

void CreateList(LinkList *L) {//����ͷ��� 
	(*L)=(LinkList )malloc(sizeof(Lnode));
	(*L)->next=NULL;
}

void totallist(LinkList &L) {//����������ֵ ���������� 
	int n,x;
	cin>>x;
	LinkList p=L;
	LinkList q;
	for(int i=0; i<x; i++) {
		q=(LinkList )malloc(sizeof(Lnode));
		q->next=NULL;
		cin>>n;
		p->num=n;
		p->next=q;
		p=p->next;
		q=0;
	}
}

LinkList hebing(LinkList a,LinkList b ) {//������������ϲ� 
	LinkList p=a,q=b,k,r;
	LinkList t;
	CreateList(&t);
	k=t;
	while((p->next!=0)&&(q->next!=0)) {
		if(p->num<=q->num) {
			k->num=p->num;
			r=(LinkList )malloc(sizeof(Lnode));
			r->next=NULL;
			k->next=r;
			k=k->next;
			r=0;
			p=p->next;
		} else if(p->num>q->num) {
			k->num=q->num;
			r=(LinkList )malloc(sizeof(Lnode));
			r->next=NULL;
			k->next=r;
			k=k->next;
			r=0;
			q=q->next;
		}
	}
	if(q->next!=0) {//��һ���������ʱ����һ�����Զ�����t�� 
		while(q!=0) {
			k->num=q->num;
			q=q->next;
			r=(LinkList )malloc(sizeof(Lnode));
			r->next=NULL;
			k->next=r;
			k=k->next;
			r=0;
		}
	} else if(p->next!=0) {
		while(p!=0) {
			k->num=p->num;
			p=p->next;
			r=(LinkList )malloc(sizeof(Lnode));
			r->next=NULL;
			k->next=r;
			k=k->next;
			r=0;
		}

	}
	return t;
}

void deal(LinkList L) {//ɾ���������ظ���Ԫ�ؽڵ� 
	LinkList p,q;
	p=L;
	q=p->next;
	while(q->next!=0) {
		if(q->num==p->num) {
			p->next=q->next;
			free(q);
			q=p->next;
		} else {
			p=q;
			q=q->next;
		}
	}
}

void show(LinkList L) {
	LinkList p=L;
	while(p->next->next!=0) {
		cout<<p->num<<' ';
		p=p->next;
	}
}

int main() {
	LinkList L1,L2,L;
	CreateList(&L1);
	CreateList(&L2);
	totallist(L1);
	totallist(L2);
	L=hebing(L1,L2);
	deal(L);
//	show(L1);
//	show(L2);
	show(L);
	free(L1);
	free(L2);
	free(L);
	return 0;
}

