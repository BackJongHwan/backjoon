#include "binary.cpp"

template<typename E>
class AVLEntry: public E{
private:
    int ht;
protected:
    typedef typename E::Key K;
    typedef typename E::Value V;
    int height() const{return ht;}
    void setHeight(int h){ht = h;}
public:
    AVLEntry(const K&k = K(), const V& v= V())
        :E(k, v),ht(0){}
    friend class AVLTree<E>;
};

template<typename E>
