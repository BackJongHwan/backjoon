#include<iostream>
#include<list>

template<typename E, typename C>
class AdaptPriorityQueue{
protected:
    typedef std::list<E> ElementList;
public:
    class Position{
    private:
        typename ElementList::iterator q;
    public:
        const E& operator*(){return *q;}
        friend class AdaptPriorityQueue;
    };
public:
    int size() const;
    bool empty() const;
    const E& min() const;
    Position insert(const E& e);
    void removeMin();
    void remove(const Poisition &p);
    Position replace(const Position &p, const E& e);
private:
    ElementList L;
    C isLess;
};
