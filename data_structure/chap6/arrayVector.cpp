#include<iostream>

template<typename E>
class ArrayVector{
public:
    ArrayVector();
    ~ArrayVector();
    int size() const;
    bool empty() const;
    const E& operator[](int i);
    const E& at(int i);
    void erase(int i);
    void insert(int i, const E& e);
    void reserve(int N);
private:
    int capacity;
    int n;
    E* A;
};

template<typename E>
ArrayVector<E>::ArrayVector()
    :capacity(0), n(0),A(NULL){}

template<typename E>
ArrayVector<E>::~ArrayVector()
{
    delete A;
}

template