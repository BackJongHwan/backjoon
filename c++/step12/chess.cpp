#include<iostream>
using namespace std;

int color_chess(char **board, int m, int n, int row, int col)
{
  char temp[8][8];
  int count1 = 0, count2 = 0;
  for(int i = 0; i < 8; i++)
      for(int j = 0; j < 8; j++)
          temp[i][j] = board[i + row][j + col];

  //temp[0][0] is black
  temp[0][0] = 'B';
  if(board[row][col] == 'W')
      count1++;
  for(int i = 0; i < 7; i++)
  {
      if(temp[i][0] == temp[i+1][0])
      {
          if(temp[i][0] == 'B')
              temp[i+1][0] = 'W';
          else temp[i+1][0] = 'B';

          count1++;
      }
    
      for(int j = 0; j < 7; j++)
      {

          if(temp[i][j] == temp[i][j+1])
          {
              if(temp[i][j] == 'B')
                  temp[i][j+1] = 'W';
              else temp[i][j+1] = 'B';
              count1++;
          }
      }
  }

  for(int i = 0; i < 8; i++)
  {
      if(temp[7][i] == temp[7][i+1])
      { 
          if(temp[7][i] == 'B')
              temp[7][i+1] = 'W';
          else temp[7][i+1] = 'B';
              count1++;
      }
  
  }

  //(0,0) is white;
  for(int i = 0; i < 8; i++)
      for(int j = 0; j < 8; j++)
          temp[i][j] = board[i + row][j + col];

  temp[0][0] = 'W';
  if(board[row][col] == 'B')

      count2++;
  for(int i = 0; i < 7; i++)
  {
      if(temp[i][0] == temp[i+1][0])
      {
          if(temp[i][0] == 'B')
              temp[i+1][0] = 'W';
          else temp[i+1][0] = 'B';
          count2++;
      }
    
      for(int j = 0; j < 7; j++)
      {

          if(temp[i][j] == temp[i][j+1])
          {
              if(temp[i][j] == 'B')
                  temp[i][j+1] = 'W';
              else temp[i][j+1] = 'B';
              count2++;
          }
      }
  }
  for(int i = 0; i < 8; i++)
  {
      if(temp[7][i] == temp[7][i+1])
      { 
          if(temp[7][i] == 'B')
              temp[7][i+1] = 'W';
          else temp[7][i+1] = 'B';

          count2++;
      }
  }

  int count = count1;
  if(count2 < count1)
      count = count2;
  return count;
}




int main()
{
   int m, n;
   int min = 64;
   cin >> m >> n;
   char **board = new char*[m];
   int count;
   for(int i = 0; i < m;i++)
   {
       board[i] = new char[n];
   }

   for(int i = 0; i < m; i++)
       for(int j = 0; j < n; j++)
           cin >> board[i][j];

   for(int i = 0; i < m - 7; i++){
       for(int j = 0; j < n - 7; j++){
           count = color_chess(board,m, n, i, j);
           if(count < min)
               min = count;
       }
       
   }

   cout << min <<endl;
}
