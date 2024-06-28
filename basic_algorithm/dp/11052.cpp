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
        cin >> arr[i];
    cut_rob2(arr,result,n);
    cout<<result[n - 1]<<'\n';
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
//solve bottom-up
void cut_rob2(int arr[], int r[],int n)
{
    int i, j, q;
    r[0] = 0;
    for(i = 0; i < n; i++){
        q = -1;
        for(j = 0; j <= i; j++)
        {
            q = max(q, arr[j] + r[i - j]);
        }
        r[i] = q;
    }
}
