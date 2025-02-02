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
        if(str[i] == ' '){
            if(i != 0 && i != str.length() - 1)
                count++;
        }
    }
    if(str.length() == 1 && str[0] == ' ')
        count = -1;

    std::cout<<count+1<<std::endl;

}
