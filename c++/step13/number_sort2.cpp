#include<iostream>
#include<algorithm>

int main()
{
    int n;
    int *arr = new int[n];
    std::cin >> n;

    for(int i = 0; i < n; i++)
    {
        std::cin >> arr[i];
    }
    std::sort(arr, arr + n);

    for(int i = 0; i < n; i++)
        std::cout << arr[i]<<'\n';

    delete [] arr;
    return 0;
}
