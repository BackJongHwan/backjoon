#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

int main()
{
    string str;
    cin >> str;
    int *arr = new int[str.length()];
    for(int i = 0; i < str.length(); i++)
        arr[i] = str[i] - '0';

    sort(arr, arr + str.length(),greater<int>());

    for(int i = 0; i < str.length(); i++)
        cout<<arr[i];
    cout<<'\n';

    return 0;

    
}
