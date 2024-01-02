#include<iostream>
using namespace std;
int main()
{
    int arr[9], max, max_index;

    max = 0;
    max_index = 0;
    for(int i = 0; i < 9; i++)
    {
        cin >> arr[i];
        if(max < arr[i]){
            max = arr[i];
            max_index = i;
        }
    }

    cout << max << endl;
    cout << max_index + 1<< endl;


    return 0;

}
