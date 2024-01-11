#include <iostream>
#include <string>
#include<cstdio>
using namespace std;

struct Node {
    int num;
    int score;
    Node* next;
};

int main() {
    Node* head = new Node;
    Node* second = new Node;
    Node* third = new Node;
    head->next = second;
    second->next = third;
    third->next = head;
    int num1, num2, num3;
    int score1, score2, score3;
    //cin >> num1 >> score1 >> num2 >> score2 >> num3 >> score3;

    scanf("%d,%d %d,%d %d,%d",&num1,&score1,&num2,&score2,&num3,&score3);
    head->num = num1;
    head->score = score1;
    second->num = num2;
    second->score = score2;
    third->num = num3;
    third->score = score3;
    cout << "[" <<"num=" << head->num << "," <<"score="<< head->score << "]" << endl;
    cout << "[" <<"num="<< second->num << "," << "score="<<second->score << "]" << endl;
    cout << "[" <<"num="<< third->num << "," <<"score="<< third->score << "]" << endl;
    return 0;
}


