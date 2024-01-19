#include<iostream>
using namespace std;

typedef string Elem;

class CNode{
private:
    Elem elem;
    CNode *next;

    friend class CicleList;
};

class CicleList{
public:
    CicleList();
    ~CicleList();
    bool empty() const;
    const Elem& front()const;
    const Elem& back()const;
    void advance();
    void add(const Elem &e);
    void remove();
    void print_current();
private:
    CNode* cursor;
};


CicleList::CicleList()
    :cursor(NULL){}
CicleList::~CicleList()
{   while(!empty()) remove();}

bool CicleList::empty() const
{
    return(cursor==NULL);
}

const Elem& CicleList::front() const
{
    return(cursor->next->elem);
}

const Elem& CicleList::back() const
{
    return(cursor->elem);
}

void CicleList::advance(){
    cursor = cursor->next;
}

void CicleList::add(const Elem &e)
{
    CNode *v = new CNode;
    v->elem = e;
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
}

void CicleList::remove()
{
    CNode *old = cursor->next;
    if(old == cursor)
        cursor = NULL;
    else
        cursor->next = old->next;
    delete old;
}

void CicleList::print_current()
{
    cout<<"current is "<<cursor->elem<<endl;
}

int main()
{
    CicleList playList;
    playList.add("Stayin Alive");
    playList.print_current();
    playList.add("Le Preak");
    playList.print_current();
    playList.add("Jive Talkin");
    playList.print_current();

    playList.advance();
    playList.print_current();
    playList.advance();
    playList.print_current();
    playList.remove();
    playList.print_current();
    playList.add("Disco Infreno");
    playList.print_current();
    return 0;
}