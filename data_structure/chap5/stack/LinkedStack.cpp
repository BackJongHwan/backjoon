#include "single_template.cpp"
template<typename E>
class SNode;

template<typename E>
class SLinkedList;

template<typename E>
class LinkedStack{
    public:
        LinkedStack();
        ~LinkedStack();
        int size() const;
        bool empty() const;
        const E& top() const;
        void push(const E& e);
        void pop();
    private:
        SLinkedList<E> S;
        int n;
};

template<typename E>
LinkedStack<E>::LinkedStack()
    :S(), n(0){
        //cout<<"constructor"<<endl;
    }


template<typename E>
LinkedStack<E>::~LinkedStack()
{
    while (!empty())
    {
        pop();
    }
    //cout<<"Decompose Linked Stack!!"<<endl;
}

template<typename E>
int LinkedStack<E>::size() const
{
    return n;
}

template<typename E>
    
bool LinkedStack<E>::empty() const
{
    return(n == 0);
}

template<typename E>
const E& LinkedStack<E>::top() const
{
    return(S.front());
}

template<typename E>
void LinkedStack<E>::push(const E& e)
{
    ++n;
    S.addFront(e);
}

template<typename E>
void LinkedStack<E>::pop()
{
    S.removeFront();
    --n;
}

