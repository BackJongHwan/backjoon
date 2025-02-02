#include<iostream>
using namespace std;

int main()
{
    int n, m, temp;
    int* box;
    int b1, b2;
    cin>> n >> m;
    box = new int[n];
    //Initialize box
    for(int i =0; i < n; i++)
    {
        box[i] = i + 1;
    }
    //change the ball m times
    for(int i = 0; i < m; i++)
    {
        cin >> b1 >> b2;
        temp = box[b1 -  1];
        box[b1 - 1] = box[b2 - 1];
        box[b2 -1] = temp;

    }
    for(int i =0; i < n; i++)
    {
        cout<<box[i]<< " ";
    }
 

    return 0;
}

