#include<iostream>

using namespace std;
int main()
{
    int arr[42] = {0,};
    int n, count = 0
        ;
    for(int i = 0; i< 10; i++){
        cin >> n;
        arr[n % 42]++;
    }

    for(int i = 0; i < 42; i++)
    {
        if(arr[i] >= 1) count++;
    }

    cout<<count<<endl;

    return 0;

    
}
