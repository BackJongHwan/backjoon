#include<iostream>
#include<string>
#include <cctype>

int main()
{
    std::string str;
    std::getline(std::cin, str);
    int count = 0;

    for(int i = 0; i < str.length(); i++)
    {
        if(str[0] ==' ') continue;
        
        if(str[i] == ' ') count++;
    }

    std::cout<<count+1<<std::endl;

}
