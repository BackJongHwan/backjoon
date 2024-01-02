#include<iostream>
#include<string>

int main()
{
    int n;
    std::cin >> n;
    for(int i = 0; i < n; i++)
    {
        std::string str;
        std::cin>> str;
        std::cout<<str[0]<< str[str.length() - 1]<<std:: endl;
    }

    return 0;
}
