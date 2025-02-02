#include "binary.cpp"
#include<algorithm>
template<typename E>
class AVLEntry: public Entry{
private:
    int ht;
protected:
    typedef typename E::Key K;
    typedef typename E::Value V;
    int height() const{return ht;}
    void setHeight(int h){ht = h;}
public:
    AVLEntry(const K&k = K(), const V& v= V())
        :Entry(k, v),ht(0){}
    friend class AVLTree<E>;
};

template<typename E>
class AVLTree: public SearchTree< AVLEntry<E> > {
public:
    typedef AVLEntry<E> AVLEntry;
    typedef typename SearchTree<AVLEntry>::Iterator Iterator;
protected:
    typedef typename AVLEntry::Key K;
    typedef typename AVLEntry::Value V;
    typedef SearchTree<AVLEntry> ST;
    typedef typename ST::TPos TPos;
public:
    AVLTree();
    Iterator insert(const K&k, const V& x);
    void erase(const K&K);
    void erase(const Iterator&p);
protected:
    int height(constr TPos &v) const;
    void setHeight(TPos v);
    bool isBalanced(const TPos &v) const;
    TPos tallGrandChild(const TPos &z) const;
    void rebalance(const TPos &v);
};

template<typename E>
AVLTree<E>::AVLTree()
    :ST(){}


template<typename E>
int AVLTree<E>::height(const TPos &v) const
{
    return(v.isExteranl() ? 0 : v->height());
}

template<typename E>
void AVLTree<E>::setHeight(TPos v)
{
    int hl = height(v.left());
    int hr = height(v.right());

    v->setheight(std::max(hl, hr) + 1);
}

template<typename E>
bool AVLTree<E>::isBalanced(const TPos &v ) const
{
    int bal = height(v.left()) - height(v.right());
    return ( -1 <= bal && bal <= 1);
}

template<typename E>
AVLTree<E>::TPos AVLTree<E>::tallGrandChild(const TPos &z) const
{
    TPos zl = z.left();
    TPos zr = z.right();
    if(height(zl) >= height(zr))
        if(height(zl.left()) >= height(zl.right()))
            return zl.left();
        else
            return zl.right();
    else
        if(height(zr.right()) >= height(zr.left()))
            return zr.right();
        else
            return zr.left();
}

template<typename E>
void AVLTree<E>::rebalance(const TPos &v)
{
    TPos z = v;
    while(!(z == ST::root()))
    {
        z = z.parent();
        setHeight(z);
        if(!isBalanced(z))
        {
            TPos x = tallGrandChild(z);
            z = restructure(x);
            setHeight(z.left());
            setHeight(z.right());
            setHeight(z);
        }
    }
}

template<typename E>
AVLTree<E>::Iterator AVLTree<E>::insert(const K&k, const V&v)
{
    TPos v = insert(k, v);
    setHeight(v);
    rebalance(v);
    return Iterator(v);
}

template<typename E>
void AVLTree<E>::erase(const K&k){
    TPos w = eraser(v);
    rebalance(w);
}

template<typename E>
void AVLTree<E>::erase(const Iterator&p){
    erase(p.v);
}