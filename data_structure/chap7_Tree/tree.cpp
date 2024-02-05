#include<iostream>
#include<algorithm>
#include<list>
template<typename E>
class Position
{
public:
    E& operator*();
    Position parent() const;
    std::list<Position> children() const;
    bool isRoot() const;
    bool isExternal() const;
};

template<typename E>
class Tree{
public:
    class Position;
public:
    int size() const;
    bool empty() const;
    Position root() const;
    std::list<Position> positions() const;
};

int main(){
    
    return 0;
}