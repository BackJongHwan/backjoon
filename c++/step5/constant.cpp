#include<iostream>
#include<string>

int main()
{
    std::string str1, str2;
    std::cin >> str1 >> str2;
    char temp1 = str1[0];
    str1[0] = str1[2];
    str1[2] = temp1;
    char temp2 = str2[0];
    str2[0] = str2[2];
    str2[2] = temp2;
    std::cout<<max(str1, str2)<<std::endl;


    return 0;

    
}
