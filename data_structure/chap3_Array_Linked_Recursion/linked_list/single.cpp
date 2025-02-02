#include<iostream>
#include<string>

class StringNode{
private:
    std::string element;
    StringNode *next;
    friend class StringLinkedList;
};

class StringLinkedList{
public:
    StringLinkedList();
    ~StringLinkedList();
    bool empty() const;
    const string& front() const;
    void addFront(const String&e);
    void removeFront();
private:
    StringNode *head;
};


StringLinkedList::StringLinkedList()
    :head(NULL){}

StringLinkedList::~StringLinkedList()
{
    while(!empty) removeFront();
}

bool StringLinkedList::empty() const
{
    return head == NULL;
}

const string& StringLinkedList::front() const
{
    return head->element;
}

void StringLinkedList::addFront(const String&e)
{
    StringNode* new_node = new StringNode;
    new_node->element = e;
    new_node->next = head;
}

void StringLinkedList::removeFront()
{
    StringNode *temp = head->next;
    delete head;
    head = temp;
}

