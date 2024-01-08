#include<iostream>
using namespace std;

int main()
{
    int n;
    int input_arr[10000] = {0,};
    int temp;
    cin >> n;
    for(int i = 0; i < n; i++)
    {
        cin >> temp;
        input_arr[temp]++;
    }
    int max = input_arr[0];
    for(int i = 0 ; i < 10000; i++)
    {
        if(max < input_arr[i])
            max = input_arr[i];
    }

    int count_arr[max] = {0, };

    for(int i = 0; i < 10000; i++)
    {
        count_arr[input_arr[i]]++;
    }

    for(int i = 1; i < max; i++)
        count_arr[i] += count_arr[i - 1];


}

