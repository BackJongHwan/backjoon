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
        int front;
        int rear;
        E* queue;
};

template<typename E>
Circle_queue::Circle_queue(int cap)
    :capacity(cap), front(0),rear(0), queue(new E[cap]){}

template<typename E>
Circle_queue::~Circle_queue()
{
    delete[] queue;
}


template<typename E>
int Circle_queue::size() const
{
    
}

template<typename E>
bool Circle_queue::empty() const
{
    return(rear == front);
}

template<typename E>
void Circle_queue::enqueue(const E& e)
{

}

template<typename E>
void Circle_queue::dequeue() 
{

}

template<typename E>
const E& Circle_queue::front() const
{
    return q[front];
}

