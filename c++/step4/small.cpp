#include<iostream>
using namespace std;
int main()
{
    int n, x, count = 0;
    cin >> n >> x;
    int *arr = new int[n];
    for(int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    for(int i = 0; i < n; i++)
    {
        if(x > arr[i]) cout<<arr[i]<<" ";
    }

    delete []arr;

    return 0;
}
