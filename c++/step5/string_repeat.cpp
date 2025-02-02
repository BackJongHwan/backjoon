#include<iostream>
#include<string>

int main()
{
    int test;
    std::cin >> test;
    for(int i = 0; i < test; i++)
    {
        int repeat;
        std::string s;
        std::cin >> repeat >> s;
            for(int k = 0; k < s.length(); k++)
            {
                for(int j = 0; j < repeat; j++)
                    std::cout << s[k];
            }

        std::cout<<'\n';
    }
}
