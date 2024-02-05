#include<iostream>
using namespace std;
typedef int E;

class Node{
private:
    E element;
    Node *prev;
    Node *next;
    friend class Deque;
};

class Deque{
public:
    Deque();
    //~Deque();
    void push_front(const E& e);
    void push_back(const E& e);
    void pop_front();
    void pop_back();
    int size() const;
    bool empty() const;
    void front() const;
    void back() const;
private:
    Node* head;
    Node* trailer;
    int n;
};

Deque::Deque(){
    head = new Node;
    trailer = new Node;
    head->next = trailer;
    trailer->prev = head;
    n = 0;
}

// Deque::~Deque(){
//     while(!empty()) pop_back();
//     delete head;
//     delete trailer;
// }

int Deque::size() const{
    return n;
}

bool Deque::empty() const{
    return (n == 0);
}

void Deque::push_front(const E& e){
    Node *v = new Node;
    v->element = e;
    v->prev = head;
    v->next = head->next;

    head->next->prev = v;
    head->next = v;
    n++;
}

void Deque::push_back(const E& e){
    Node *v = new Node;
    v->element = e;
    v->next = trailer;
    v->prev = trailer->prev;
    trailer->prev->next = v;
    trailer->prev = v;
    n++;
}

void Deque::pop_back(){
    if(empty())
        cout<<-1<<endl;
    else{
        Node *old = trailer->prev;
        cout<<old->element<<endl;
        old->prev->next = trailer;
        trailer->prev = old->prev;
        delete old;
        n--;
    }
}

void Deque::pop_front(){
    if(empty())
        cout<<-1<<endl;
    else
    {
        Node *old = head->next;
        cout<<old->element<<endl;
        head->next = old->next;
        old->next->prev = head;
        delete old;
        n--;
    }

}

void Deque::front() const{
    if(empty())
        cout<<-1<<endl;
    else
        cout<<head->next->element<<endl;
}

void Deque::back() const{
    if(empty())
        cout<<-1<<endl;
    else cout<<trailer->prev->element<<endl;
}

int main(){
    Deque D;
    int n;
    string str;
    cin >> n;
    for(int i = 0; i < n; i++)
    {
        cin >> str;
        if(str =="push_front")
        {
            int k;
            cin >> k;
            D.push_front(k);
        }
        else if(str == "push_back")
        {
            int k;
            cin >> k;
            D.push_back(k);
        }
        else if(str == "pop_front")
        {
            D.pop_front();
        }
        else if(str =="pop_back"){
            D.pop_back();
        }
        else if(str == "size")
        {
            cout<<D.size()<<endl;
        }
        else if(str =="empty")
        {
            if(D.empty()) cout<<1<<endl;
            else cout<<0<<endl;
        }
        else if(str ==  "front"){
            D.front();
        }
        else if(str == "back"){
            D.back();
        }
    }
    return 0;
}