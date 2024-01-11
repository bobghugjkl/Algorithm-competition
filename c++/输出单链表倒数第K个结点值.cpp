#include<stdio.h>

#include<stdlib.h>
int count = 0;
typedef struct node
{
    int m_nkey;
    struct node* m_pNext;
}Node;

//������������
Node* creatList()
{
    Node* headNode = (Node*)malloc(sizeof(Node));
    headNode->m_pNext = NULL;
    return headNode;
}
//�������
Node* creatNode(int m_nkey)
{
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->m_nkey = m_nkey;
    newNode->m_pNext = NULL;
    return newNode;
}
//��β������
void insertByBack(Node* headNode, int m_nkey)
{
    Node* newNode = creatNode(m_nkey);
    Node* pMove = headNode;
    while (pMove->m_pNext != NULL)
    {
        pMove = pMove->m_pNext;
    }
    pMove->m_pNext = newNode;
    count++; //ÿ����һ����㣬�ڵ���+1
}
//��ȡ������k������ֵ
int getNodeValue(Node* headNode, int k)
{
    if (k > count || k==0) return NULL;
    Node* pMove = headNode;

    for (int i = 0; i < (count - k +1); i++) //������k�� = �����ڣ�count - k +1��
    {
        pMove = pMove->m_pNext;
    }

    return pMove->m_nkey;
}

int main()
{
    int num;//���������
    int val;//ÿ�����ֵ
    int k;  //Ҫ���صĵ�����k���ڵ�ֵ
    //��������ͷ�ڵ�
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


