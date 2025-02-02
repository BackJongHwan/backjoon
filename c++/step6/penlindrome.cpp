#include<iostream>
#include<string>

int main()
{
    std::string str;
    std::cin >> str;
    int pelindrome = 1;
    for(int i = 0; i< str.length()/2 ; i++)
    {
        if(str[i] != str[str.length()- 1 - i])
        {
            pelindrome = 0;
            break;
        }

    }
    std::cout<< pelindrome<<std::endl;

    return 0;

}
