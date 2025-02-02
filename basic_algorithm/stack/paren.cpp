#include<iostream>
#include<stack>
using namespace std;

int main()
{
    int n;
    int vaild;
    cin >>n;
    string str;
    stack<char> stack;
    for(int i = 0; i < n; i++)
    {
        cin >> str;
        while(!stack.empty()) 
            stack.pop();
        vaild = 1;
        for(int j = 0; j < str.length(); j++)
        {
            if(str[j] == '('){
                stack.push('(');
            }
            else{
                if(stack.empty())
                {
                    vaild = 0;
                }
                else{
                    stack.pop();
                }
            }
        }

        if(!stack.empty()) vaild = 0;
        if(vaild) cout<<"YES"<<endl;
        else cout<<"NO"<<endl;
    }
    return 0;
}