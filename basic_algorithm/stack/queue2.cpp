
#include<queue>
using namespace std;

int main(){
    queue<int> Q;
    string str;
    int n;
    cin >> n;
    for(int i = 0; i < n; i++)
    {
        cin >> str;
        if(str == "push"){
            int k;
            cin >> k;
            Q.push(k);
        }else if(str == "front"){
            if(Q.empty()) cout<<-1<<endl;
            else cout<<Q.front()<<endl;
        }else if(str == "back"){
            if(Q.empty()) cout<<-1<<endl;
            else cout<<Q.back()<<endl;
        }else if(str == "empty"){
            if(Q.empty()) cout<<1<<endl;
            else cout<<0<<endl;
        }else if(str == "pop"){
            if(Q.empty()) cout<<-1<<endl;
            else{
                cout<<Q.front()<<endl;
                Q.pop();
            }
        }else if(str =="size"){
            cout<<Q.size()<<endl;
        }
    }
    return 0;
}