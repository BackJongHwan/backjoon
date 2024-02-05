#include<iostream>
#include<string>
using namespace std;
typedef int E;

struct Node
{
    E element;
    Node *next;
};

class Queue{
public:
    Queue();
    // ~Queue();
    void push(const E& e);
    void pop();
    int size() const;
    bool empty() const;
    void front() const;
    void back() const;
    void advance() ;
private:
    Node* cursor;
    int n;
};

Queue::Queue()
    :cursor(NULL), n(0){}

// Queue::~Queue()
// {
//     while(!empty())
//     {
//         pop();
//     }
// }

void Queue::pop()
{
    if(empty())
        cout<<-1<<'\n';
    else{
        cout<<cursor->next->element<<endl;
        Node* old = cursor->next;
        if(old == cursor){
            cursor == NULL;
        }else{
            cursor->next = old->next;
        }
        delete old;
        n--;
    }
    
}

void Queue::advance(){
    cursor = cursor->next;
}

bool Queue::empty() const{
    return (n == 0);
}

void Queue::front() const{
    if(empty()) cout<<-1<<'\n';
    else
    {
        if(size() != 1)
            cout<<cursor->next->element<<'\n';
        else
            cout<<cursor->element<<'\n';
    }
}

void Queue::back() const{
    if(empty()) cout<<-1<<'\n';
    else cout<<cursor->element<<endl;
}

void Queue::push(const E& e){
    Node *v = new Node;
    v->element = e;
    if(empty()){
        v->next = v;
        cursor = v;
    }else{
        v->next = cursor->next;
        cursor->next = v;
    }
    advance();
    n++;
}
int Queue::size() const
{
    return n;
}

int main()
{
    int n;
    cin >> n;
    string str;
    Queue Q;
    for(int i = 0; i < n; i++)
    {
        cin >> str;
        if(str == "push"){
            int k;
            cin >> k;
            Q.push(k);
        }else if(str == "front"){
            Q.front();
        }else if(str == "back"){
            Q.back();
        }else if(str == "empty"){
            if(Q.empty()) cout<< 1<<'\n';
            else cout<<0<<'\n';
        }else if(str == "pop"){
            Q.pop();
        }else{
            cout<<Q.size()<<endl;
        }
    }
    return 0;
}