#include<iostream>

int main()
{
    int leap;
    std::cin>>leap;
    if(leap % 4 == 0){
        if(leap % 100 != 0 || leap % 400 == 0)
            std::cout<<1<<std::endl;
        else
            std::cout<<0<<std::endl;
    }
    else
        std::cout<<0<<std::endl;
    return 0;
}
