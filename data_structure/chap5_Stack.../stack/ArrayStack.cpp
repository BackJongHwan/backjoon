#include<iostream>
#include<string>
#include <typeinfo>
using namespace std;
class RuntimeException { // generic run-time exception
private:
    string errorMsg;
public:
    RuntimeException(const string& err) { errorMsg = err; }
    string getMessage() const { return errorMsg; }
};

class StackEmpty : public RuntimeException{
    public:
    StackEmpty(const string &err): RuntimeException(err){}
};

class StackFull : public RuntimeException{
    public:
    StackFull(const string &err): RuntimeException(err){}
};


template<typename E>
class ArrayStack{
    enum{DEF_CAPACITY = 100};
    public:
        ArrayStack(int cap, const string& name);
        ~ArrayStack();
        int size() const;
        const E& top() const ;
        bool empty() const;
        void pop() ;
        void push(const E& e);

    private:
        string name;
        E* stack;
        int capacity;
        int t; 
};

template<typename E>
ArrayStack<E>::ArrayStack(int cap, const string& name)
    :stack(new E[cap]), capacity(cap), t(-1) {
        this->name = name;
        cout<<"call " <<this->name<< " constructor"<<endl;
    }

template<typename E>
ArrayStack<E>::~ArrayStack()
{
    cout<<"call "<<this->name <<" Destructor"<<endl;
    delete []stack;
}



template<typename E>
int ArrayStack<E>::size() const
{
    return t + 1;
}

template<typename E>
const E& ArrayStack<E>::top() const 
{
    if(empty()) 
        throw StackEmpty("Stack is Empty!!\n");
    return stack[t];
}

template<typename E>
bool ArrayStack<E>::empty() const
{
    return(t < 0);
}

template<typename E>
void ArrayStack<E>::pop() 
{
    if(empty())
        throw StackEmpty("Stack is Empty!!\n");
    t--;
}

template<typename E>
void ArrayStack<E>::push(const E& e) 
{
    if(size() == capacity)
        throw StackFull("stack is full!!\n");
    t++;
    stack[t] = e;
}

int main()
{
    ArrayStack<int> A(100, "A");
    A.push(7);
    A.push(13);
    cout<<A.top()<<endl; A.pop();
    A.push(9);
    cout<<A.top()<<endl;;
    cout<<A.top()<<endl; A.pop();
    ArrayStack<string> B(10, "B");
    B.push("Bob");
    B.push("Alice");
    cout<<B.top()<<endl; B.pop();
    B.push("Eve");

    return 0;
}