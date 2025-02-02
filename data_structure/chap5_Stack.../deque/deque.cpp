#include<iostream>
using namespace std;
template<typename E>
class DLinkedList;

template<typename E>
class Node{
    private:
    E elem;
    Node<E> *next;
    Node<E> *prev;
    friend class DLinkedList<E>;
};

template<typename E>
class DLinkedList{
    public:
        DLinkedList();
        ~DLinkedList();
        int size() const;
        bool empty() const;
        const E& front() const;
        const E& back() const;
        void addFront(const E& e);
        void addBack(const E& e);
        void removeFront();
        void removeBack();
    private:
        Node<E> *head;
        Node<E> *trailer;
        int n;
    protected:
        void add(Node<E> *v, const E&e);
        void remove(Node<E> *v);
};

template<typename E>
class LinkedDeque
{
    public:
        LinkedDeque();
        ~LinkedDeque();
        int size() const;
        bool empty() const;
        const E& front() const;
        const E& back() const;
        void insertFront(const E&);
        void insertBack(const E&);
        void removeFront();
        void removeBack();
    private:
        DLinkedList<E> D;
        int n;
};

template<typename E>
DLinkedList<E>::DLinkedList()
    :n(0)
    {
        head = new Node<E>;
        trailer = new Node<E>;
        head->next = trailer;
        trailer->prev = head;
    }

template<typename E>
DLinkedList<E>::~DLinkedList()
{
    while(!empty())
    {
        removeFront();
    }
    delete head;
    delete trailer;
}

template<typename E>
int DLinkedList<E>::size() const{
    return n;
}
template<typename E>
bool DLinkedList<E>::empty() const{
    return (n==0);
}
template<typename E>
const E& DLinkedList<E>::front() const{
    return (head->next->elem);
}
template<typename E>
const E& DLinkedList<E>::back() const{
    return(trailer->prev->elem);
}

template<typename E>
void DLinkedList<E>::addFront(const E& e)
{
    add(head->next, e);
}

template<typename E>
void DLinkedList<E>::addBack(const E& e) 
{
    add(trailer, e);
}

template<typename E>
void DLinkedList<E>::removeBack()
{
    remove(trailer->prev);
}

template<typename E>
void DLinkedList<E>::removeFront()
{
    remove(head->next);
}

template<typename E>
void DLinkedList<E>::add(Node<E> *v, const E& e)
{
    Node<E> *new_node = new Node<E>;
    new_node->elem = e;
    new_node->next = v;
    new_node->prev = v->prev;
    new_node->prev->next = new_node;
    v->prev = new_node;
}

template<typename E>
void DLinkedList<E>::remove(Node<E> *v)
{
    v->prev->next = v->next;
    v->next->prev = v->prev;
    delete v;
}

template<typename E>
LinkedDeque<E>::LinkedDeque()
    :D(),n(0){}

template<typename E>
LinkedDeque<E>::~LinkedDeque()
{
    while(!empty())
    {
        removeFront();
    }
}

template<typename E>
int LinkedDeque<E>::size() const
{
    return n;
}
template<typename E>
bool LinkedDeque<E>::empty() const{
    return (n == 0);

}
template<typename E>
const E& LinkedDeque<E>::front() const{
    return(D.front());
}
template<typename E>
const E&LinkedDeque<E>::back() const{
    return(D.back());
}
template<typename E>
void LinkedDeque<E>::insertFront(const E& e)
{
    D.addFront(e);
    n++;
}
template<typename E>
void LinkedDeque<E>::insertBack(const E& e)
{
    D.addBack(e);
    n++;
}

template<typename E>
void LinkedDeque<E>::removeFront()
{
    D.removeFront();
    n--;
}

template<typename E>
void LinkedDeque<E>::removeBack()
{
    D.removeBack();
    n--;
}

int main()
{
    LinkedDeque<int> Q;
    Q.insertFront(3);
    Q.insertFront(5);
    Q.insertBack(19);
    cout<<Q.size()<<endl;
    return 0;
}