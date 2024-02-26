
// template<typename E>
// class BinaryTree{

// };


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
        
    };
};