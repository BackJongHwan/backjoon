#include<iostream>
#define MAX_SIZE 1000
using namespace std;

int main()
{
    int n;
    int num;
    cin >>  n;
    int arr[MAX_SIZE];
    arr[1] = 1;
    arr[2] = 3;
    for(int i = 3; i < MAX_SIZE + 1; i++){
        arr[i] = arr[i - 1] + 2* arr[i - 2];
        arr[i] %= 10007;
    }
    cout<<arr[n]<<'\n';
    return 0;
}