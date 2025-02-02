#include<iostream>
#include<string>

int main()
{
    std::string str[100];
    int i;
    for(i = 0; i < 100; i++)
    {
        std::getline(std::cin, str[i]);
        if(str[i] == "") break;
    }

    for(int j = 0; j < i; j++)
    {
        std::cout<<str[j]<<std::endl;
    }

    return 0;


}
