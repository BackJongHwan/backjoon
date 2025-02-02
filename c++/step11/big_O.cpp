#include<iostream>
using namespace std;
bool succes(int a1, int a0, int c, int n0);

int main()
{
    int a1, a0, c, n0;
    cin >> a1 >> a0 >> c >> n0;
    if(succes(a1, a0, c, n0))
        cout<<1<<endl;
    else cout<<0<<endl;
}


bool succes(int a1, int a0, int c, int n0)
{
    if(a1 * n0 + a0 > c * n0)
        return 0;
    else return 1;
}

