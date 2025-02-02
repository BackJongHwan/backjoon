#include<iostream>
#include<string>

int main()
{
    std::string word;
    std::cin >> word;
    int num = word.length();

    for(int i = 0; i < word.length(); i++)
    {
        if(word[i] == '-')
        {
            num--;
        }
        if(word[i] == 'j')
        {
            if(i > 0)
                if(word[i-1] == 'l' || word[i -1] == 'n')
                    num--;
        }
        if(word[i] == '=')
        {
            if(i > 1){
                if(word[i -2] == 'd' && word[i -1] == 'z')
                    num -=2;
                else if(word[i -1] == 'c' ||word[i -1] == 's' ||word[i -1] == 'z' )
                    num--;
            }
            else if( i > 0)
                if(word[i -1] == 'c' ||word[i -1] == 's' ||word[i -1] == 'z' )
                    num--;
        }
    }

    std::cout<<num<<std::endl;
}
