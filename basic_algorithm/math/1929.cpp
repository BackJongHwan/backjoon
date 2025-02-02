#include<iostream>
using namespace std;


int main()
{
    int m, n;
    int check = 2;
    cin >> m >> n;
    int arr[n + 1];
    //if arr[i] == 1 then i is prime
    for(int i = 1; i < n + 1; i++)
        arr[i] = 1;
    while(check < n + 1)
    {
        if(arr[check] == 1)
        {
            int j = 2;
            while(check * j < n + 1)
            {
                arr[check * j] = 0;
                j++;
            }
        }
        check++;
    }
    arr[1] = 0;
    for(int i = m; i < n + 1; i++)
    {
        if(arr[i] == 1)
            cout<<i<<'\n';
    }
}