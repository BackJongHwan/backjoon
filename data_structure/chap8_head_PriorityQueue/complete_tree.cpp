#include<iostream>
#include<vector>
using namespace std;
template<typename E>
class VetorCompleteTree{
    private:
        vector<E> V;
    public:
        typedef typename vector<E>::iterator Position;
    protected:
        Position pos(int i)
        {   return V.begin() + i; }
        int idx(const Position &p)
        { return p - V.begin();}
public:
    VetorCompleteTree() : V(1){}
    int size() const {return V.size() - 1; }
    Position left(const Position &p) {return pos(2*idx(p));}
    Position right(const Position &p) {return pos(2 * idx(p) + 1);}
    Position parent(const Position &p) {return pos(idx(p) / 2);}
    bool hasLeft(const Position &p) { return 2 * ipx(p) <= size();}
    bool hasRight(const Position &p){return 2 * ipx(p) + 1 <= size();}
    bool isRoot(const Position &p){ return ipx(p) == 1}
    Position root(){return pos(1);}
    Position last(){return pos(size());}
    void addLast(const E& e){ V.push_back(e); }
    void removeLast(){ V.pop_back();}
    void swap(const Position &p, const Position &q){ E e = *p; *p = *q; *q = e;}
};

int main(){
    VetorCompleteTree<int> heap;
    return 0;
}
