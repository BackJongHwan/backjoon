#include<iostream>
#include<stack>
#include<queue>
using namespace std;

void sequence(int arr[], int n)
{
    stack<int> S;
    queue<char> Q;
    int push = 0;
    int valid = 1;
    for(int i = 0; i < n; i++){
        if(arr[i] > push + 1){
            for(push; push <arr[i]; push++)
            {
                S.push(push + 1);
                Q.push('+');
            }
            S.pop();
            Q.push('-');
        }
        else if(arr[i] == push + 1){
            Q.push('+');
            Q.push('-');
            push++;
        }
        else{
            if(S.top() == arr[i]){
                Q.push('-');
                S.pop();
            }else{
                valid = 0;
                break;
            }
        }
    }
    if(valid == 0)
    {
        cout<<"NO"<<'\n';
    }
    else{
        while(!Q.empty())
        {
            cout<<Q.front()<<'\n';
            Q.pop();
        }
    }
}
int main(){
    int n;
    cin>>n;
    int arr[n];
    for(int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    sequence(arr, n);
    return 0;
}