#include<iostream>
using namespace std;
int main()
{
    char toy [5][15];
    string str ="";
    char temp;

    for(int i = 0; i < 5; i++)
    {
        cin >> toy[i];
    }

    for(int j = 0; j < 15; j++)
    {
        if(toy[0][j] == NULL)
            break;
        for(int i =0; i < 5; i++)
        {
            if(toy[i][j] != ' ')
                str += toy[i][j];
        }
    }
    cout<<str<<endl;

}
