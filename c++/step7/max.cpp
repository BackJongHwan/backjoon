#include<iostream>
using namespace std;
#define SIZE 9
int main()
{
    int matrix[SIZE][SIZE];
    //input maxtric value
    for(int i = 0; i < SIZE; i++)
    {
        for(int j = 0; j < SIZE; j++)
        {
            cin >> matrix[i][j];
        }
    }

    //find the max
    int max = 0;
    int row, col;
    for(int i = 0; i < SIZE; i++)
    {
        for(int j = 0; j < SIZE; j++)
        {
            if(matrix[i][j] >= max)
            {
                max = matrix[i][j];
                row = i + 1;
                col = j + 1;
            }

        }
    }

    cout<<max<<endl;
    cout<<row <<" "<< col << endl;

}
