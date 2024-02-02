#include<iostream>
template<typename E>
class stack{
public:
    stack()
        :element(new E[capacity]), t(-1), capacity(100){}

    ~stack()
    {    delete element; }
    void push(E &e)
    {
        if(size() == capacity)
        {
            capacity *= 2;
            E *temp = new E[capacity];
            for(int i = 0; i < size(); i++)
            {
                temp[i] = element[i];
            }
            delete element;
            temp = element;
        }
        element[++t] = e;
    }
    void pop()
    {
        if(empty()) std::cout<<-1<<'\n';
        else{
            std::cout<<element[t]<<'\n';
            t--;
        }
    }

    int size() const
    {
        return (t + 1);
    }

    bool empty() const
    {
        return (t < 0);
    }
    E& top() const
    {
        return element[t];
    }
private:
    E *element;
    int t;
    int capacity;
};

int main(){
    int n;
    std::cin >> n;
    stack<int> S;
    for(int i = 0; i < n; i++)
    {
        std::string str;
        std::cin >> str;
        int k;
        if(str == "push"){
            std::cin>>k;
            S.push(k);
        }
        else if(str == "top"){
            std::cout<<S.top()<<'\n';
        }
        else if(str == "size"){
            std::cout<<S.size()<<'\n';
        }
        else if(str == "pop"){
            S.pop();
        }
        else if(str == "empty"){
            if(S.empty())
                std::cout<<1<<'\n';
            else
                std::cout<<0<<'\n';
        }
    }
    return 0;
}