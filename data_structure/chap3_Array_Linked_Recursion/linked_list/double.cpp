#include<iostrema>
#include<string>
using namespace std;

typedef string Elem;

class DNode{
private:
    Elem elem;
    DNode* prev;
    DNode* next;
    friend class DLinkedList;
};

class DLinkedList{
public:
    DLinkedList();
    ~DLinkedList();
    bool empty() const;
    const Elem & front() const;
    const Elem & back() const;
    void addFront(const Elem&e);
    void addBack(const Elem&e);
    void removeFront():
    void removeBack();
private:
    DNode* header;
    DNode* trailer;
protected:
    void add(DNode *v, const Elem&e);
    void remove(DNode *v);
};

DLinkedList::DLinkedList()
{
    header = new DNode;
    trailer = new DNode;
    header->next = trailer;
    trailer->prev = header;
}

DLinkedList::~DLinkedList()
{
    while(!empty()) removeFront();
    delete header;
    delete trailer;
}

bool DLinkedList::empty()
{
    return(header->next == trailer);
}


const Elem & DLinkedList::front() const
{
    return(header->next->elem);
}

const Elem & DLinkedList::back() const
{
    return(trailer->prev->elem);
}

void DLinkedList::addFront(const Elem&e)
{
    add(header->next, e);
}

void DLinkedList::addBack(const Elem&e)
{
    add(trailer, e);
}

void DLinkedList::removeFront()
{
    remove(header->next);
}

void DLinkedList::removeBack()
{
    remove(trailer->prev);
}

void DLinkedList::add(DNode *v, const Elem&e)
{
    DNode *u = new DNode;
    u->elem = e;
    u->next = v;
    u->prev = v->prev;
    u->prev->next = u;
    v->prev = u->prev;
}

void DLinkedList::remove(DNode *v)
{
    DNode* u = v->prev;
    DNode* w = v->next;
    u->next = w;
    w->prev = u;
    delete v; 
}

