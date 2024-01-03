#include<iostream>
#include<string>

int main()
{
    int n, group = 0;
    std::cin >> n;
    group = n;

    for(int i =0 ; i< n; i++)
    {
        std::string str;
        std::cin>>str;
        int alpha[26] = {0,};
        int is = 1;
        //overlap..
        for(int j = 0; j < str.length() - 1; j++)
        {
            if(str[j] != str[j+1])
                alpha[int(str[j]) - int('a')]++;
            if(alpha[int(str[j + 1]) - int('a')] > 0)
            {
                is = 0;
                break;
            }

        }

        for(int j = 0; j < 26; j++)
        {
            if(alpha[j] > 1){
                is = 0;
                break;
            }
        }

        if(str[str.length() -1] != str[str.length() -2] && alpha[int(str[str.length() - 1]) - int('a')] > 0)
            is  = 0;

        if(is == 0)
            group--;
    }


    std::cout<<group<<std::endl;
}
