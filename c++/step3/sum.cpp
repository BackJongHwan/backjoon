#include<iostream>
using namespace std;

int main()
{
    int n, sum;
    sum = 0;
    cin >> n;
    for(int i = 1; i < n + 1; i++)
    {
        sum += i;
    }

    cout<< sum << endl;
    return 0;
}
