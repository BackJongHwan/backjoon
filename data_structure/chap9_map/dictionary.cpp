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
