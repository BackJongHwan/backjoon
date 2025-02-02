#include<iostream>
#include<algorithm>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n;
    int two = 0; int five = 0;
    for(int i = 1; i < n +1; i++)
    {
        int temp = i;
        while(true)
        {
            if(temp % 5 == 0)
            {
                five++;
                temp /= 5;
            }
            if(temp % 2 == 0)
            {
                two++;
                temp /= 2;
            }
            if(temp % 5 != 0 && temp % 2 != 0) break;
        }
    }
    cout<<min(two, five)<<'\n';
}