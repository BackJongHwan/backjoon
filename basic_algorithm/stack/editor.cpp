#include<iostream>
#include<string>
using namespace std;
class editor{
public:
    editor(const string &str2){
        this->str = str2;
        cursor = str2.size();
    }
    void left(){
        if(cursor == 0){
            cursor = 0;
        }else{
            cursor--;
        }
    }
    void right(){
        if(cursor != str.size())
        {
            cursor++;
        }
    }
    void Delete(){
        if(cursor != 0)
        {
            str.erase(cursor - 1, 1);
            cursor--;
        }
    }
    void add(const string& ch){
        if(cursor == str.size()){
            str += ch;
            cursor++;
        } 
        else if(str != "") str.insert(cursor, ch);
        if(str == ""){
            str += ch;
            cursor = 0;
        }
    }
    void print(){
        cout<<str<<endl;
        //cout<<cursor<<endl;
    }
private:
    int cursor;
    string str;
};
int main()
{
    string str;
    char cmd;
    int n;
    cin >> str;
    cin >> n;
    editor editor(str);
    for(int i = 0; i < n; i++){
        cin >> cmd;
        if(cmd == 'L'){
            editor.left();
        }else if(cmd == 'D'){
            editor.right();
        }else if(cmd == 'B'){
            editor.Delete();
        }else if(cmd == 'P'){
            string ch;
            cin >> ch;
            editor.add(ch);
        }
        //editor.print();
    }
    editor.print();
    return 0;
}