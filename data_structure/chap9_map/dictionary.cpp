#include "hash.cpp"

template<typename K, typename V,typename H>
class HashDict : public HashMap<K, V, H>{
public:
    typedef typename HashMap<K, V, H>::Iterator Iterator;
    typedef typename HashMap<K, V, H>::Entry Entry;
    class Range{
    public:
        Iterator _begin;
        Iterator _end;
    public:
        Range(const Iterator& b, const Iterator& e)
            :_begin(b), _end(e){}
        Iterator& begin(){  return _begin;  }
        Iterator& end(){    return _end;    }
    };
public:
    HashDict(int capacity = 100);
    Range findAll(const K& k);
    Iterator insert(const K&k, const V& v);
};

template<typename K, typename V, typename H>
HashDict<K, V, H>::HashDict(int capacity)
    :HashMap<K, V, H>(capacity){}

template<typename K, typename V, typename H>
typename HashDict<K, V, H>::Iterator HashDict<K, V, H>::insert(const K& k, const V&v){
    Iterator p = finder(k);
    Iterator q = inserter(p, Entry(k, v));
}

template<typename K, typename V, typename H>
typename HashDict<K, V, H>::Range HashDict<K, V, H>::findAll(const K& k)
{
    Iterator p = finder(k);
    Iterator q = p;
    while(!endofBkt(q) &&(*q).key() == (*p).key())
        ++q;
    return Range(p, q);
}

