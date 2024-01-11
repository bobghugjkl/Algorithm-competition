#include<stdio.h>

#include<stdlib.h>
int count = 0;
typedef struct node
{
    int m_nkey;
    struct node* m_pNext;
}Node;

//创建单向链表
Node* creatList()
{
    Node* headNode = (Node*)malloc(sizeof(Node));
    headNode->m_pNext = NULL;
    return headNode;
}
//创建结点
Node* creatNode(int m_nkey)
{
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->m_nkey = m_nkey;
    newNode->m_pNext = NULL;
    return newNode;
}
//表尾插入结点
void insertByBack(Node* headNode, int m_nkey)
{
    Node* newNode = creatNode(m_nkey);
    Node* pMove = headNode;
    while (pMove->m_pNext != NULL)
    {
        pMove = pMove->m_pNext;
    }
    pMove->m_pNext = newNode;
    count++; //每插入一个结点，节点数+1
}
//获取倒数第k个结点的值
int getNodeValue(Node* headNode, int k)
{
    if (k > count || k==0) return NULL;
    Node* pMove = headNode;

    for (int i = 0; i < (count - k +1); i++) //倒数第k个 = 整数第（count - k +1）
    {
        pMove = pMove->m_pNext;
    }

    return pMove->m_nkey;
}

int main()
{
    int num;//输入结点个数
    int val;//每个结点值
    int k;  //要返回的倒数第k个节点值
    //创建链表头节点
    Node* headNode = creatList();

    while (scanf("%d", &num) != EOF)
    {
        for (int i = 0; i < num; i++)
        {
            scanf("%d", &val);
            insertByBack(headNode, val);
        }
        scanf("%d", &k);
        printf("%d\n", getNodeValue(headNode, k));
    }
}


