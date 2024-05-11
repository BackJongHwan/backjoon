#include<iostream>
using namespace std;
int arr[12];
int main()
{
    arr[1] = 1;
    arr[2] = 2;
    arr[3] = 4;
    for(int i = 4; i < 12; i++)
    {
        arr[i] = arr[i -3] + arr[i-2] + arr[i -1];
    }
    int n;
    int num;
    cin >> n;
    for(int i = 0; i < n; i++)
    {
        cin>>num;
        cout<<arr[num]<<'\n';
    }
    return 0;
}