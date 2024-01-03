#include<iostream>

int main()
{
    int black[6] = {1, 1, 2 ,2, 2, 8};
    int white[6];
    for(int i = 0; i < 6; i++)
        std::cin >> white[i];
    for(int i = 0; i < 6; i++)
        white[i] =  black[i] - white[i];
    for(int i = 0; i < 6; i++)
        std::cout<< white[i]<<" ";
    std::cout<<'\n';
}
