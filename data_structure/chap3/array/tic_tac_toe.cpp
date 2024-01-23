#include<iostream>
#include<vector>
using namespace std;
const int X = -1, EMPTY = 0, O = 1;

int board[3][3];
int currentPlayer;
void clearBoard()
{
    for(int i = 0; i < 3; i++)
        for(int j = 0; j < 3; j++)
            board[i][j] = EMPTY;
    currentPlayer = X;
}

void putMark(int row, int col)
{
    board[row][col] = currentPlayer;
    currentPlayer *= -1;
}

bool isWin(int player)
{
    int win = 3 * player;
    return(
        //row
    (board[0][0] + board[0][1] + board[0][2] == win)
    || (board[1][0] + board[1][1] + board[1][2] == win)
    || (board[2][0] + board[2][1] + board[2][2] == win)
    //col
    || (board[0][0] + board[1][0] + board[2][0] == win)
    || (board[0][1] + board[1][1] + board[2][1] == win)
    || (board[0][2] + board[1][2] + board[2][2] == win)
    //diagonadl
    || (board[0][0] + board[1][1] + board[2][2] == win)
    || (board[0][2] + board[1][1] + board[2][0] == win)
    );
}

bool fullBoard()
{
    for(int i = 0; i < 3; i++)
     for(int j = 0; j < 3; j++)
        if(board[i][j] == EMPTY)
            return false;
    return true;
}

int getWinner()
{
    if(isWin(X)) return X;
    else if(isWin(O)) return O;
    else return 0;
}

void printBoard()
{
    for(int i = 0; i < 3; i++)
    {
        for(int j = 0; j < 3; j++)
        {
            switch (board[i][j])
            {
            case X:
                cout<<"X";
                break;
            case O:
                cout<<"O";
                break;
            default:
                cout<<" ";
                break;
            }
            if(j < 2) cout<<"|";
        }
        if(i < 3) cout<<"\n-+-+-\n";
    }
}

int main()
{
    int gameset = 1;

    while(gameset)
    {
        clearBoard();

        while((!fullBoard()) && (getWinner() == 0))
        {
            int row, col = 0;
            if(currentPlayer == X)
            {
                cout<<"Player X: ";
                cin>> row >> col;
                putMark(row, col);
            }
            else{
                cout<<"Player O: ";
                cin>> row >> col;
                putMark(row, col);
            }
            int Winner = getWinner();
            printBoard();

            if(Winner != 0)
            {
                cout<<"Winner is "<<(Winner == X? 'X' : 'O')<<endl;
                break;
            }
        }
        if(fullBoard())
            cout<<"board is full"<<endl;
        cout<<"continue(1): ";
        cin>>gameset;
    }
}
