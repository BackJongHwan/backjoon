#include<iostream>
using namespace std;
int main()
{
    int n, v, count = 0;
    cin >> n;
    int *arr = new int[n];
    for(int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    cin >> v;
    for(int i = 0; i < n; i++)
    {
        if(v == arr[i]) count++;

    }

    cout << count<<endl;
    delete []arr;

    return 0;
}
