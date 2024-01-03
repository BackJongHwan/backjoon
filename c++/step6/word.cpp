#include<iostream>
#include<string>
using namespace std;

int main()
{
    string str;
    cin>>str;
    int alpha[26] = {0,};
    //find the number of alphabets in string 
    for(int i = 0; i < str.length(); i++)
    {
        if(int('a')<=int(str[i])&&int(str[i])<=int('z'))
        {
            alpha[int(str[i]) - int('a')]++;
        }

        if(int('A')<= int(str[i])&&int(str[i])<=int('Z'))
        {
            alpha[int(str[i]) - int('A')]++;
        }
    }

//    for(int i = 0; i < 26; i++)
//    {
//        cout<<alpha[i] <<" ";
//    }
    int max = 0;
    for(int i = 0; i < 26; i++)
    {
        if(alpha[i] > max)
            max = alpha[i];
    }
    int max_count = 0;
    int index = 0;
    for(int i = 0; i < 26; i++)
    {
        if(alpha[i] == max){
            max_count++;
            index = i;
        }
    }
    if(max_count == 1){
        cout<<char(index + int('A'))<<endl;
    }else{
        cout<<'?'<<endl;
    } 
}
