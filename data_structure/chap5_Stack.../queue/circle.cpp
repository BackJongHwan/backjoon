#include<iostream>
using namespace std;

template<typename E>
class Circle_queue
{
    enum {DEF_CAPACITY = 100};
    public:
        Circle_queue(int cap = DEF_CAPACITY);
        ~Circle_queue();
        int size() const;
        bool empty() const;
        void enqueue(const E& e);
        void dequeue();
        const E& front() const;
    private:
        int capacity;
        int f;
        int rear;
        E* queue;
};

template<typename E>
Circle_queue<E>::Circle_queue(int cap)
    :capacity(cap + 1), f(0),rear(0), queue(new E[cap + 1]){}

template<typename E>
Circle_queue<E>::~Circle_queue()
{
    delete[] queue;
}


template<typename E>
int Circle_queue<E>::size() const
{
    if(rear >= f) 
        return rear - f;
    else
        rear + capacity - f;
}

template<typename E>
bool Circle_queue<E>::empty() const
{
    return(rear == f);
}

template<typename E>
void Circle_queue<E>::enqueue(const E& e)
{
    if(((rear + 1) % capacity) == f)
        cout<<"full of queue"<<endl;
    else{
        queue[rear] = e;
        rear = (rear + 1) % capacity;
    }
}

template<typename E>
void Circle_queue<E>::dequeue() 
{
    if(empty()){
        cout<<"Queue is empty!!"<<endl;
    }
    else{
        f = (f + 1) % capacity;
    }
}

template<typename E>
const E& Circle_queue<E>::front() const
{
    return queue[f];
}


int main()
{
    Circle_queue<int> q(8);
    cout<<"queue size: "<<q.size()<<endl;
    //q.dequeue();
    q.enqueue(0);
    q.enqueue(1);
    cout<<"front: "<<q.front()<<endl;
    //q.dequeue();
    cout<<"front: "<<q.front()<<endl;
    q.enqueue(2);
    //q.dequeue();
    cout<<"front: "<<q.front()<<endl;
    q.enqueue(3);
    q.enqueue(4);
    cout<<"front: "<<q.front()<<endl;
    q.enqueue(5);
    q.enqueue(6);
    q.enqueue(7);
    q.enqueue(8);
    for(int i = 0; i < 10; i++)
        q.dequeue();
    cout<<"queue size: "<<q.size()<<endl;
    return 0;
}
