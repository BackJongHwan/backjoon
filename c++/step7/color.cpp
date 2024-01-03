#include<iostream>

using namespace std;

int main()
{
    bool board[100][100] = {false};
    //0 is white 1 is black
    int num_black, x, y;
    cin >> num_black;
    for(int i = 0; i < num_black; i++)
    {
        cin >> x >> y;
        for(int j = 0; j < 10; j++)
            for(int k = 0; k < 10; k++)
                board[x + j][y + k] = true;
    }

    int black = 0;
    for(int i = 0; i < 100; i++)
        for(int j =0; j < 100; j++)
            if(board[i][j] == 1)
                black++;
    cout<<black<<endl;

}
