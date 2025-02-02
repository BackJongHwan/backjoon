#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int *arr = new int[n];
    vector<int> v;
    for(int i = 0; i < n; i++)
    {
        cin >> arr[i];
        v.push_back(arr[i]);
    }
    sort(v.begin(), v.end());
    v.erase(unique(v.begin(), v.end()), v.end());
    for(int i = 0; i < n; i++)
    {
        auto it = lower_bound(v.begin(), v.end(), arr[i]);
        int index = it -  v.begin();
        cout << index << " ";
    }
    cout<<'\n';
   
    delete[] arr;
    return 0;
}
