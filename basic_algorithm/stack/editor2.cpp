#include<iostream>
#include<string>
using namespace std;

typedef char E;

class Node{
private:
    E element;
    Node *next;
    Node *prev;
    friend class DoubleLinkedList;
};

class DoubleLinkedList{
public:
    DoubleLinkedList(){
        head = new Node;
        trailer = new Node;
        head->next = trailer;
        trailer->prev = head;
        (*cursor) = head;
    }

    void left(){
        
    }

    void right(){

    }

    void Delete(){

    }

    void add(const char& ch)
    {

    }
private:
    Node *head;
    Node *trailer;
    Node **cursor;
};

int main()
{
    string str;
    char cmd;
    int n;
    cin >> str;
    cin >> n;
    for(int i = 0; i < n; i++)
    {
        cin >> cmd;
        if(cmd == 'L'){

        }else if(cmd == 'D'){
        }else if(cmd == 'B'){
        }else if(cmd == 'P'){
            char ch;
            cin >> ch;
        }
    }
    return 0;
}