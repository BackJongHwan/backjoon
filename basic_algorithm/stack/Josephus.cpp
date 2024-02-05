#include<iostream>
using namespace std;

typedef int E;
class Node{
private:
    E name;
    Node*next;
    friend class Circle;
};  

class Circle{
public:
    Circle();
    //~Circle();
    void advance();
    void eliminate();
    void add(const E& e);
private:
    Node* cursor;
};

Circle::Circle()
    :cursor(NULL){}

void Circle::advance(){
    cursor = cursor->next;
}

void Circle::eliminate(){
    Node *old = cursor->next;
    if(old == cursor)
    {
        cursor == NULL;
    }else{
        cursor->next = old->next;
    }
    cout<<old->name;
    delete old;
}

void Circle::add(const E& e){
    Node *v = new Node;
    v->name = e;
    if(cursor == NULL){
        v->next = v;
        cursor = v;
    }else{
        v->next = cursor->next;
        cursor->next = v;
        cursor = v;
    }
}

int main()
{
    int n, k;
    cin >> n >> k;
    Circle circle;
    for(int i = 0; i < n; i++)
    {
        circle.add(i + 1);
    }
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < k - 1; j++)
        {
            circle.advance();
        }
        if(i == 0) cout<<"<";
        circle.eliminate();
        if(i != n - 1) cout<<", ";
        else cout<<">"<<'\n';
    }
    return 0;
}