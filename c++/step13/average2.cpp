#include<iostream>
using namespace std;
int main()
{
    int arr[5];
    int sum = 0;
    for(int i = 0; i < 5; i++)
    {
        cin >> arr[i];
        sum += arr[i];
    }
    int min;
    int temp;
    int min_index;
    for(int i = 0; i < 4; i++)
    {
        min = arr[i];
        min_index = i;
        for(int j = i; j < 5; j++)
        {
            if(arr[j] < min)
            {
                min = arr[j];
                min_index = j;
            }
        }
        temp = arr[i];
        arr[i] = min;
        arr[min_index] = temp;
    }

    cout<<sum / 5<<endl;
    cout<<arr[2]<<endl;
    
}
