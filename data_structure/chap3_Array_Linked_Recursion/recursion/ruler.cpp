#include<iostream>
using namespace std;

void drawOneTick(int tickLength, int tickLabel = -1)
{
    for(int i = 0; i < tickLength; i++)
        cout<<"-";
    if(tickLabel >= 0) cout<<" "<<tickLabel;
    cout<<"\n";
}

void drawTicks(int tickLength)
{
    if(tickLength > 0)
    {
        drawTicks( tickLength -1);
        drawOneTick(tickLength);
        drawTicks( tickLength -1);
    }
}

void drwaRuler(int nlnches, int majorLength)
{
    drawOneTick(majorLength, 0);
    for(int i = 1;  i < nlnches + 1; i++)
    {
        drawTicks(majorLength - 1);
        drawOneTick(majorLength, i);
    }
}




int main()
{
    int a, b;
    cin >> a >> b;
    drwaRuler(a, b);
    return 0;
}