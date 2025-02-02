#include<iostream>
using namespace std;

int main()
{
    int side[3], max, max_index;
    for(int i = 0; i < 3; i++)
        cin >>side[i];
    max = side[0];
    max_index = 0;

    if(side[1] > max)
    {
        max = side[1];
        max_index =  1;
    }

    if(side[2] > max)
    {
        max = side[2];
        max_index =  2;
    }
    int temp = max;
    while(true)
    {
        if(max < side[0] + side[1] + side[2] - temp)
            break;
        else max--;
    }

    cout<<side[0] + side[1] + side[2] - temp + max<<endl;
    
}

