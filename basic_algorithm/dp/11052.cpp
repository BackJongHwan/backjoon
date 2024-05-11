#include<iostream>
#include<algorithm>
using namespace std;
int cut_rob(int arr[], int n);
void cut_rob2(int arr[], int result[], int n);

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int n, i;
    cin>>n;
    int arr[n];
    int result[n];
    for(i = 0; i < n; i++)
        result[i] = -1;
    for(i = 0; i < n; i++)
        cin >> arr[i];
    cut_rob2(arr, result ,n );
    int max = 0;
    for(i = 0; i < n; i++)
    {
        if(max < result[i])
            max = result[i];
    }
    cout<<max<<'\n';
    return 0;
}
/*solve recursively not memorization*/
int cut_rob(int arr[], int n)
{
    if(n == 0)
        return 0;
    int q = -1;
    for(int i = 0; i < n; i++)
        q = max(q, arr[i] + cut_rob(arr, n - (i + 1)));
    return q;
}
//solve using memorazation
void cut_rob2(int arr[], int result[], int n)
{
    int i;
}