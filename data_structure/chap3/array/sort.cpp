#include<iostream>
using namespace std;
void insertion_sort(char *A)
{
    for(int i = 1; i < 5; i++)
    {
        char cur = A[i];
        int j = i - 1;
        while(j >= 0 && A[j] > cur)
        {
            A[j + 1] = A[j];
            j--;
        }
        A[j + 1] = cur;
    }
}
int main()
{
    char arr[] = {'a', 'e', 'v', 'i', 'c'};
    insertion_sort(arr);


    for(int i = 0; i < 5; i++)
        cout<<arr[i]<<" ";
    cout<<endl;
}