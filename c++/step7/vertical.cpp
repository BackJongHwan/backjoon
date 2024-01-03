#include<iostream>
using namespace std;

int main()
{
    char toy[5][15];
    for(int i = 0; i < 5; i++)
        for(int j = 0; j < 15; j++)
            toy[i][j] = '\n';
    for(int i = 0; i < 5; i++)
        cin >> toy[i];
    for(int j =0 ; j < 15; j++)
        for(int i = 0; i < 5; i++)
            if(('A'<=toy[i][j] && toy[i][j] <= 'Z')||('a'<=toy[i][j] && toy[i][j]<= 'z')||('0'<=toy[i][j] && toy[i][j] <= '9'))
                {
                    cout<<toy[i][j];
                }

}
