#include<iostream>

using namespace std;

int main()
{
    int hour, min;
    cin >> hour >> min;
    if(min < 45)
    {
        if(hour  == 0)
            hour = 23;
        else hour -= 1;

        min += 15;
    }
    else min -= 45;

    cout<<hour<<" " << min << endl;

    return 0;
}
