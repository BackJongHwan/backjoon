#include<iostream>
#include<vector>

int main(){
    std::vector<int> stack;
    int n;
    std::cin >> n;
    for(int i = 0; i < n; i++)
    {
        std::string str;
        std::cin >> str;
        int k;
        if(str == "push"){
            std::cin>>k;
            stack.push_back(k);
        }
        else if(str == "top"){
            if(stack.empty())
            {
                std::cout<<-1<<std::endl;
            }else
            {
                std::cout<<stack.back()<<std::endl;
            }
        }
        else if(str == "size"){
            std::cout<<stack.size()<<std::endl;
        }
        else if(str == "pop"){
            if(stack.empty())
            {
                std::cout<<-1<<std::endl;
            }else{
                std::cout<<stack.back()<<std::endl;
                stack.erase(stack.begin() + stack.size() - 1);
            }
        }
        else if(str == "empty"){
            if(stack.empty())
                std::cout<<1<<'\n';
            else
                std::cout<<0<<'\n';
        }
    }
    return 0;
}