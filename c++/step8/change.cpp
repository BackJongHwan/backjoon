#include<iostream>
using namespace std;

enum Change{
    QUARTER = 25,
    DIME = 10,
    NICKEL = 5,
    PENNY = 1,
};
int main()
{
    int n;
    int a, b, c, d;
    cin >> n;
    for(int i = 0; i < n; i++)
    {
        int money;
        cin >> money;
        a = 0, b =0, c = 0, d =0;
        if(money >= QUARTER)
        {
            a = money / QUARTER;
            money %= QUARTER;
        }

        if(money >= DIME)
        {
            b = money / DIME;
            money %= DIME;
        }

        if(money >= NICKEL)
        {
            c = money / NICKEL;
            money %= NICKEL;
        }

        if(money >= PENNY)
        {
            d = money / PENNY;
            money %= PENNY;
        }

        cout<<a<<" "<<b<<" "<<c<<" "<<d<<endl;

        

            
    }
    return 0;
}
