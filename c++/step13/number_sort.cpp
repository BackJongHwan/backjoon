#include<iostream>
//#include<algorithm>

//int main()
//{
//    int n;
//    int *arr;
//    std::cin >> n;
//    arr = new int[n];
//    for(int i = 0; i < n; i++)
//        std::cin >> arr[i];
//    std::sort(arr, arr + n);
//    for(int i = 0; i < n; i++)
//        std::cout<<arr[i]<<'\n';
//}

int main()
{
    int n;
    int *arr;
    std::cin >> n;
    arr = new int[n];
    for(int i = 0; i < n; i++)
        std::cin >> arr[i];
    for(int i = 0; i < n - 1; i++)
        for(int j = i + 1 ; j < n; j++)
            if(arr[i] > arr[j])
            {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
    for(int i = 0; i < n; i++)
        std::cout<<arr[i]<<'\n';
    return 0;
}

