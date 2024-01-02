#include<iostream>
#include<string>


int main()
{
    std::string str;
    std::cin >> str;
    int time = 0;

    for(int i = 0; i <str.length(); i++)
    {
        if(str[i] - 'A' < int('P' - 'A'))
            time += (str[i] - 'A') / 3 + 3;
        else if(str[i] - 'P' >= 0 && str[i] - 'S' <= 0)
            time += (str[i] - 'P') / 4 + 8; 
        else if(str[i] - 'T' >= 0 && str[i] - 'V' <= 0)
            time += (str[i] - 'T') /3 + 9;
        else
            time += (str[i] - 'W') / 4 + 10;
    }

    std::cout<<time<<std::endl;
}
