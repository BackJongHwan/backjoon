#include<iostream>
#include<vector>
using  std::vector;

template<typename E>
class NodeList{
private:
    template<typename U>
    struct Node
    {
        U elem;
        Node *prev;
        Node *next;
    };
public:
    template<typename R>
    class Iterator
    {
    public:
        R& operator*();
        bool operator ==(const Iterator& p) const;
        bool operator !=(const Iterator& p) const;
        Iterator& operator++();
        Iterator& operator--();
        Iterator& operator++(int);
        void print() const;
        friend class NodeList;
    private:
        Node<R> *v;
        Iterator(Node<R> *u);
        Iterator();
    };
public:
    NodeList();
    int size() const;
    bool empty() const;
    Iterator<E> begin() const;
    Iterator<E> end() const;
    void insertFront(const E& e);
    void insertBack(const E& e);
    void insert(const Iterator<E> &p, const E& e);
    void eraseFront();
    void eraseBack();
    void erase(const Iterator<E> &p);
    void print_all() const;
private:
    int n;
    Node<E> *header;
    Node<E> *trailer;
};



template<typename E>
template<typename R>
NodeList<E>::Iterator<R>::Iterator(Node<R> *u)
{   v = u;  }


template<typename E>
template<typename R>
NodeList<E>::Iterator<R>::Iterator()
{
    v = nullptr;
}

template<typename E>
template<typename R>
R& NodeList<E>::Iterator<R>::operator*()
{return v->elem;}
template<typename E>
template<typename R>
void NodeList<E>::Iterator<R>::print() const
{
    std::cout<<v->elem<<std::endl;
}

template<typename E>
template<typename R>
bool NodeList<E>::Iterator<R>::operator==(const Iterator<R> &p) const
{return v == p.v;}

template<typename E>
template<typename R>
bool NodeList<E>::Iterator<R>::operator!=(const Iterator<R> &p) const
{return v != p.v;}

template<typename E>
template<typename R>
NodeList<E>::Iterator<R>& NodeList<E>::Iterator<R>::operator++()
{   
    v = v->next; 
    return *this;
}


template<typename E>
template<typename R>
NodeList<E>::Iterator<R>& NodeList<E>::Iterator<R>::operator++(int)
{
    auto *temp = this;
    this->operator++();
    return *temp;
}

template<typename E>
template<typename R>
NodeList<E>::Iterator<R>& NodeList<E>::Iterator<R>::operator--()
{v = v->prev; return *this;}

template<typename E>
NodeList<E>::NodeList()
{
    n = 0;
    header = new Node<E>;
    trailer = new Node<E>;
    header->next = trailer;
    trailer->prev = header;
}

template<typename E>
int NodeList<E>::size() const
{return n;}

template<typename E>
bool NodeList<E>::empty() const
{return (n == 0);}

template<typename E>
NodeList<E>::Iterator<E> NodeList<E>::begin() const
{ return Iterator(header->next);}

template<typename E>
NodeList<E>::Iterator<E> NodeList<E>::end() const
{ return Iterator(trailer);}

template<typename E>
void NodeList<E>::insertFront(const E& e)
{
    insert(begin(), e);
}

template<typename E>
void NodeList<E>::insertBack(const E& e)
{
    insert(end(), e);
}

template<typename E>
void NodeList<E>::insert(const NodeList<E>::Iterator<E> &p, const E& e)
{
    Node<E> *w = p.v;
    Node<E> *u = w->prev;
    Node<E> *v = new Node<E>;
    v->elem = e;
    //
    u->next = v; v->prev = u;

    v->next = w; w->prev = v; 
    n++;
}

template<typename E>
void NodeList<E>::erase(const NodeList<E>::Iterator<E> &p)
{
    Node<E> *v = p.v;
    Node<E> *w = v->next;
    Node<E> *u = v->prev;
    u->next = w;
    w->prev = u;
    delete v;
    n--;
}

template<typename E>
void NodeList<E>::eraseFront()
{
    erase(begin());
}

template<typename E>
void NodeList<E>::eraseBack()
{
    erase(--end());
}

template<typename E>
void NodeList<E>::print_all() const
{
    Iterator<E> it(begin());
    for(it; it != end(); it++)
    {
        std::cout<<*it<<std::endl;
    }
}

// int main()
// {
//     vector<int> c;
//     c.push_back(3);
//     vector<int>::iterator it3;
//     it3 = c.begin();
//     std::cout<<*it3<<std::endl;
//     NodeList<int> list;
//     NodeList<int>::Iterator<int> it(list.begin());
//     NodeList<int>::Iterator<int> it2(list.begin());
//     list.insertBack(3);
//     list.insertFront(5);
//     list.insertFront(10);
//     it = list.begin();
//     //++it;
//     it2 = it++;
//     list.print_all();

//     std::cout<<(*it2)<<std::endl;
//     std::cout<<(*it)<<std::endl;
//     return 0;
// }
