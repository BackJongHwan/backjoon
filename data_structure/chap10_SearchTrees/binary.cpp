#include<list>

template<typename E>
class BinaryTree{
protected:
    struct Node
    {
        E elt;
        Node *par;
        Node *left;
        Node *right;
        Node():elt(), par(NULL),left(NULL), right(NULL){}
    };
public:
    class Position{
    private:
        Node *v;
    public:
        Position(Node* _v = NULL) : _v(v){}
        E& operator *()
        {   return v->elt;  }
        Position left() const{
            return Position(v->left);
        }
        Position right() const{
            return Position(v->right);
        }
        Position parent() const
        {   return Position(v->par);}
        bool isRoot() const
        {   return v->par == NULL;}
        bool isExternal() const
        {   return v->left == NULL && v->right == NULL;}
        bool isInternal() const{
            return !isExternal();
        }
        friend class BinaryTree;
    };
    typedef std::list<Position> PositionList;
    public:
        BinaryTree()
            :_root(NULL), n(0){}
        int size() const
        {   return n;}
        bool empty() const
        {   return size()==0;}
        Position root() const
        {
            return Position(_root);
        }
        PositionList positions() const
        {
            PositionList pl;
            preorder(_root, pl);
            return pl;
        }
        void addRoot()
        {
            if(_root != NULL) return;
            _root = new Node;
            n = 1;
        }
        void expandExteranl(const Position &p){
            if(p.isExternal()){
                Node *v = p.v;
                v->right = new Node; v->right->par = v;
                v->left = new Node; v->left->par = v;
                n += 2;
            }
        }
        Position removeAboveExteranl(const Position &p)
        {
            if(p.isExternal())
            {
                Node *w = p.v;
                Node *v = w->par;
                Node *sib = (v->left == w? v->right : v->left);
                if(v->par == NULL)
                {
                    _root = sib;
                    sib->par = NULL;
                }else{
                    Node *gpar = v->par;
                    if(v == gpar->left)
                    {
                        gpar->left = sib;
                    }else{
                        gpar->right = sib;
                    }
                }
                delete w; delete v;
                n -= 2;
                return Position(sib);
            }
            return 0;
        }
    protected:
        void preorder(Node *v, PositionList& pl) const
        {
            pl.push_back(Position(v));
            if(v->left != NULL)
                preorder(v->left, pl);
            if(v->right != NULL)
                preorder(v->right, pl);
        }
    private:
        Node* _root;
        int n;
};


template <typename K, typename V>
class Entry{
public:
    typedef K Key;
    typedef V Value;
public:
    Entry(const K& k = K(), const V& v = V())
        :_key(k), _value(v){}
    const K& key() const{return _key;}
    const V& value() const{return _value;}
    void setKey(const K& k){ _key = k;}
    void setValue(const V& v){ _value = v;}
private:
    K _key;
    V _value;
};

template<typename E>
class SearchTree{
public:
    typedef typename E::Key K;
    typedef typename E::Value V;
    class Iterator;
public:
    SearchTree();
    int size() const;
    bool empty() const;
    Iterator find(const K& k);
    Iterator insert(const K& k, const V& v);
    void erase(const K&k);
    void erase(const Iterator&p);
    Iterator begin();
    Iterator end();
protected:
    typedef BinaryTree<E> BinaryTree;
    typedef typename BinaryTree::Position TPos;
    TPos root() const;
    TPos finder(const K& k, const TPos&v);
    TPos inserter(const K&k, const V&x);
    TPos eraser(TPos &v);
    TPos restructure(const TPos &v);
private:
    BinaryTree T;
    int n;
public:
    class Iterator{
    private:
        TPos v;
    public:
        Iterator(const TPos &vv) :v(vv){}
        const E& operator *() const{return *v;}
        E& operator *() {return *v;}
        bool operator ==(const Iterator&p) const
        {   return v== p.v;}
        Iterator& operator++();
        friend class SearchTree;
    };
};

template<typename E>
typename SearchTree<E>::Iterator& SearchTree<E>::Iterator::operator++()
{
    TPos w = v.right();
    if(w.isExternal())
    {
        w = v.parent();
        while(v == w.right())
        {
            v = w; w = w.parent();
        }
        v = w;
    }else{
        do(v = w; w = v.left();)
        while(w.isInteranl())
    }
    return *this;
}

template<typename E>
SearchTree<E>::SearchTree() 
    :T(), n(0)
{
    T.addRoot(); T.expandExteranl(T.root());
}

template<typename E>
SearchTree<E>::TPos SearchTree<E>::root() const
{
    return  T.root().left(); 
}

template<typename E>
typename SearchTree<E>::Iterator SearchTree<E>::Iterator::begin(){
    TPos v = root();
    while(v.isInternal()) v = v.left();
    return Iterator(v.parent());
}

template<typename E>
typename SearchTree<E>::Iterator SearchTree<E>::end()
{
    return Iterator(T.root());
}

template<typename E>
typename SearchTree<E>::TPos SearchTree<E>::finder(const K&k, const TPos &v)
{
    if(v.isExternal()) return v;
    if(k < v->key()) return finder(k, v.left());
    else if(k > v->key()) return finder(k, v.right());
    else return v;
}

template<typename E>
SearchTree<E>::Iterator SearchTree<E>::insert(const K&k , const V& v)
{
    TPos v = finder(k, root());
    if(v.isInternal()) return Iterator(v);
    else return end();
}

template<typename E>
SearchTree<E>::TPos SearchTree<E>::inserter(const K& k, const V& x)
{
    TPos v = finder(k, root());
    while(v.isInteranl())
        v = finder(k, v.right());
    T.expandExteranl(v);
    v->setKey(k); v->setValue(x);
    n++;
    return v;
}

template<typename E>
SearchTree<E>::Iterator SearchTree<E>::insert(const K&k, const V& x)
{
    TPos v = inserter(k, x); return Iterator(v);
}

template<typename E>
SearchTree<E>::TPos SearchTree<E>::eraser(TPos &v)
{
    TPos w;
    if(v.left().isExteranl()) w = v.left();
    else if(v.right().isExternal()) w = v.right();
    else{
        w = v.right();
        do{ w = w.left()} while(w.isInternal());
        TPos u = w.parent();
        v->setKey(u->key()); v->setValue(u->value());
    }
    n--;
    return T.removeAboveExteranl(w);
}

template<typename E>
void SearchTree<E>::erase(const K&k)
{
    TPos v = finder(k, root());
    eraser(v);
}

template<typename E>
void SearchTree<E>::erase(const Iterator& p)
{
    eraser(p.v);
}

template<typename E>
SearchTree<E>::TPos SearchTree<E>::restructure(const TPos &x)
{
    TPos y = x.parent();
    TPos z = y.parent();
    TPos a, b, c;
    if(y.left() == x){
        if(z.left() == y)
        {
            a = x; b = y; c = z;
        }
        else{
            a = z; b = x; c = y;
        }
    }else{
        if(z.left() == y)
        {
            a = y; b = x; c = z;
        }else{
            a = z; b = y; c = x;
        }
    }

}