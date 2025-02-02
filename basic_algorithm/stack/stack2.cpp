#include<iostream>
using namespace std;

template<typename E>
struct Node
{
    E element;
    Node<E>* next;
};

template<typename E>
class Stack{
public:
    Stack();
    ~Stack();
    bool empty() const;
    int size() const;
    void push(const E& e);
    void pop();
    E& top() const;
private:
    int n;
    Node<E> *head;
};

template<typename E>
Stack<E>::Stack()
    :n(0), head(NULL){}
template<typename E>
Stack<E>::~Stack()
{
    while(!empty()) pop();
}

template<typename E>
bool Stack<E>::empty() const
{
    return(n == 0);
}

template<typename E>
int Stack<E>::size() const{
    return n;
}

template<typename E>
void Stack<E>::push(const E& e)
{
    if(empty())
    {
        head = new Node<E>;
        head->next = NULL;
        head->element = e;
    }
    else{
        Node<E> *new_node = new Node<E>;
        new_node->element = e;
        new_node->next = head;
        head = new_node;
    }
    n++;
}

template<typename E>
void Stack<E>::pop(){
    if(empty())
        cout<<-1<<endl;
    else{
        cout<<head->element<<endl;
        if(size() == 1)
        {
            delete head;
        }else{
            Node<E> *old = head;
            head = old->next;
            delete old;
        }
        n--;
    }
}

template<typename E>
E& Stack<E>::top() const
{
}

int main()
{
    int n;
    cin >> n;
    Stack<int> S;
    for(int i = 0; i < n; i++)
    {
        string str;
        cin >> str;
        int k;
        if(str == "push"){
            cin>>k;
            S.push(k);
        }
        else if(str == "top"){
            cout<<S.top()<<'\n';
        }
        else if(str == "size"){
            if(S.empty())
                cout<<-1<<endl;
            else{
                cout<<S.top()<<endl;
            }
        }
        else if(str == "pop"){
            S.pop();
        }
        else if(str == "empty"){
            if(S.empty())
                cout<<1<<'\n';
            else
                cout<<0<<'\n';
        }
    }
    return 0;
}