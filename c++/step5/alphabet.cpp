#include<iostream>
#include<string>


int main()
{
    std::string s;
    int arr[26];
    for(int i = 0; i < 26; i++){
        arr[i] = -1;
    }
    std::cin >> s;
    for(int i = 0; i < s.length();i++)
    {
        if(arr[s[i] - 'a'] == -1) arr[s[i] - 'a'] = i;
        else continue;
    }

    for(int i = 0; i < 26; i++)
    {
        std::cout<<arr[i] << " ";
    }

    std::cout<<std::endl;
}
