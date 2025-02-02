#include<iostream>
#include<algorithm>
#define MAX 1000000
using namespace std;

int arr[MAX];
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);  
    int n;
    arr[1] = 0;
    cin>>n;
    for(int i = 2; i < n + 1; i++)
    {
        if(i % 6 == 0)
        {
            arr[i] = min(arr[i -1], arr[i / 3]);
            arr[i] = min(arr[i], arr[i/2]) +1;
        }
        else if(i % 3 == 0){
            arr[i] = min(arr[i -1], arr[i/3]) + 1;
        }else if(i % 2== 0){
            arr[i] = min(arr[i -1], arr[i/2]) + 1;
        }else{
            arr[i] =arr[i-1] + 1;
        }
    }
    cout<<arr[n]<<'\n';
    return 0;
}