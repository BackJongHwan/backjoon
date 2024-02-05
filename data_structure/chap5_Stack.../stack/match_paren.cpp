#include"LinkedStack.cpp"

class ParenMatch : public LinkedStack<string>{
    public:
        ParenMatch(const string& str);
        ~ParenMatch();
        bool match();
    private:
        string str;
        LinkedStack<char> S;
};

ParenMatch::ParenMatch(const string &str)
{
    this->str = str;
}

ParenMatch::~ParenMatch()
{
    S.~LinkedStack();
}

bool ParenMatch::match()
{
    for(int i = 0; i < str.length(); i++)
    {
        if(str[i] == '{' || str[i] == '[' || str[i] == '(')
        {
            S.push(str[i]);
            //cout<<str[i]<<endl;
        }
        else {
                if(S.top() == '{')
                {
                    if(str[i] != '}')
                        return false;
                }
                else if(S.top() == '[')
                {
                    if(str[i] != ']')
                        return false;

                }
                else{
                    if(str[i] != ')')
                        return false;
                }
                S.pop();
            }
        if(S.empty())
            return true;
        else return false;
    }
}



int main()
{
    ParenMatch A("(");
    if(A.match())
        cout<<"match!!"<<endl;
    else cout<<"not match!!"<<endl;
    return 0;
}