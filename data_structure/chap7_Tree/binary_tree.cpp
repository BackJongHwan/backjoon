#include<iostream>
#include<list>

typedef int Elem;

class LinkedBinaryTree{
protected:
    struct Node
    {
        Elem elt;
        Node *par;
        Node* left;
        Node* right;
        Node() : elt(), par(NULL), left(NULL), right(NULL){}
    };
public:
    class Position{
    private:
        Node *v;
    public:
        Position(Node *_v = NULL) :v(_v){}
        Elem& operator *()
        { return v->elt;}
        Position left() const
        { return Position(v->left);}
        Position right() const
        { return Position(v->right);}
        Position parent() const
        { return Position(v->par);}
        bool isRoot() const
        { return v->par == NULL;}
        bool isExternal() const
        { return v->left == NULL && v-> right == NULL;}
        friend class LinkedBinaryTree;
    };
    typedef std::list<Position> PositionList;
    public:
        LinkedBinaryTree();
        int size() const;
        bool empty() const;
        Position root() const;
        PositionList positions() const;
        void addRoot();
        void expandExternal(const Position &p);
        Position removeAboveExteranl(const Position &p);
    protected:
        void preorder(Node *v, PositionList &pl) const;
    private:
        Node* _root;
        int n;
};

LinkedBinaryTree::LinkedBinaryTree()
    :_root(NULL), n(0){}

int LinkedBinaryTree::size() const
{
     return n;
}

bool LinkedBinaryTree::empty() const
{
    return(n == 0);
}

LinkedBinaryTree::Position LinkedBinaryTree::root() const
{
    return Position(_root);
}

LinkedBinaryTree::PositionList LinkedBinaryTree::positions() const
{
    PositionList pl;
    preorder(_root, pl);
    return pl;
}

void LinkedBinaryTree::addRoot()
{
    if(_root != NULL) return;
    _root = new Node;
    n = 1;
}

void LinkedBinaryTree::expandExternal(const Position &p)
{
    if(p.isExternal())
    {
        Node *v = p.v;
        v->left = new Node; v->left->par = v;
        v->right = new Node; v->right->par = v;
        n += 2;
    }
}

LinkedBinaryTree::Position LinkedBinaryTree::removeAboveExteranl(const Position &p)
{
    if(p.isExternal())
    {
        Node *w = p.v;
        Node *v = w->par;
        Node *sib = (v->left == w ? v->right : v->left);
        if(v->par == NULL){
            _root = sib;
            sib->par = NULL;
        }
        else{
            Node *grandpar = v->par;
            if(v == grandpar->left){
                grandpar->left = sib;
            }
            else{
                grandpar->right = sib;
            }
            sib->par = grandpar;
        }
        delete w; delete v;
        n -= 2;
        return Position(sib);
    }
    return 0;
}

void LinkedBinaryTree::preorder(Node *v, PositionList &pl) const
{
    pl.push_back(Position(v));
    if(v->left != NULL)
        preorder(v->left, pl);
    if(v->right != NULL)
        preorder(v->right, pl);
}