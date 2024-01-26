#include<iostream>
using namespace std;

template<typename E>
class Node;

template<typename E>
class CicleList{
public:
    CicleList();
    ~CicleList();
    bool empty() const;
    int size() const;
    const E& front()const;
    const E& back()const;
    void advance();
    void add(const E &e);
    void remove();
private:
    Node<E>* cursor;
    int n;
};

template<typename E>
class Node{
private:
    E element;
    Node<E> *next;
    friend class CicleList<E>;
};

template<typename E>
CicleList<E>::CicleList()
    :cursor(NULL), n(0){}

template<typename E>
CicleList<E>::~CicleList()
{   while(!empty()) remove();}


template<typename E>
int CicleList<E>::size() const
{
    return n;
}
template<typename E>
bool CicleList<E>::empty() const
{
    return(cursor==NULL);
}

template<typename E>
const E& CicleList<E>::front() const
{
    return(cursor->next->element);
}

template<typename E>
const E& CicleList<E>::back() const
{
    return(cursor->element);
}

template<typename E>
void CicleList<E>::advance(){
    cursor = cursor->next;
}

template<typename E>
void CicleList<E>::add(const E &e)
{
    Node<E> *v = new Node<E>;
    v->element = e;
    if(this->empty())
    {
        v->next = v;
        cursor = v;
    }
    else
    {
        v->next = cursor->next;
        cursor->next = v;
    }
    advance();
    n++;
}

template<typename E>
void CicleList<E>::remove()
{
    Node<E> *old = cursor->next;
    if(old == cursor)
        cursor = NULL;
    else
        cursor->next = old->next;
    delete old;
    n--;
}

template<typename E>
class LinkedQueue
{
    public:
        LinkedQueue();
        ~LinkedQueue();
        int size() const;
        bool empty() const;
        void enqueue(const E& e);
        const E& front() const;
        void dequeue();
    private:
        CicleList<E> S;
};

template<typename E>
LinkedQueue<E>::LinkedQueue()
    :S(){}

template<typename E>
LinkedQueue<E>::~LinkedQueue()
{
    while(!empty())
    {
        dequeue();
    }
}

template<typename E>
int LinkedQueue<E>::size() const 
{
    return S.size();
}

template<typename E>
bool LinkedQueue<E>::empty() const
{
    return(S.size() == 0);
}

template<typename E>
void LinkedQueue<E>::enqueue(const E& e)
{
    S.add(e);
    //S.advance();
}

template<typename E>
const E& LinkedQueue<E>:: front() const
{
    return(S.front());
    
}

template<typename E>
void LinkedQueue<E>:: dequeue()
{
    S.remove();
}

int main()
{
    LinkedQueue<int> q;
    cout<<q.size()<<endl;
    q.enqueue(3);
    q.enqueue(5);
    cout<<q.size()<<endl;
    cout<<q.front()<<endl;
    q.dequeue();
    cout<<q.size()<<endl;
    cout<<q.front()<<endl;
}






