#include<iostream>
#include<stack>
#include<string>
using namespace std;

int main()
{
    int n;
    string s;
    cin>>n; stack<char> stack;
    cin.ignore();  
    for(int i = 0; i < n ; i++)
    {
        getline(cin, s);
        s += ' ';
        for(int j = 0; j < s.size(); j++)
        {
           
            if(s[j] == ' ')
            {
                while(!stack.empty())
                {
                    cout<<stack.top();
                    stack.pop();
                }
                cout<<' ';
            }else{
                stack.push(s[j]);
            }
        }
        cout<<'\n';

    }
    return 0;
}