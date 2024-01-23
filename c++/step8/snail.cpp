#include<iostream>
using namespace std;

int main()
{
    int a, b, v;
    int day = 1;
    int gap;
    cin >> a >> b >> v;
    gap = a - b;

    if((v - a) >= gap)
    {
        day += (v - a) / gap;
        if((v-a) % gap != 0)
            day++;
    }

    else
        day = 2;
    if(v == a)
        day = 1;
    cout<<day<<endl;
    return 0;
}
