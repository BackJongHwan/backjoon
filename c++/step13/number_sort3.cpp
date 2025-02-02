#include<iostream>
using namespace std;

int main()
{
    ios::sync_with_stdio(0); // false
    cin.tie(0); // NULL
    cout.tie(NULL); // 0
    int n;
    //Initialize input array
    int input_arr[10001] = {0,};
    //0 ~ 10000
    int temp;
    cin >> n;
    int max = 0; 

    for(int i = 0; i < n; i++)
    {
        cin >> temp;
        input_arr[temp]++;
        if(max < temp)
            max = temp;
    }

    for(int i = 0; i < max + 1; i++)
         for(int j = 0; j < input_arr[i]; j++)
             cout<<i<<endl;
    return 0;
}

