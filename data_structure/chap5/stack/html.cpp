#include "LinkedStack.cpp"

#include<vector>
using namespace std;

vector<string> getHtmlTags(){
    vector<string> tags;
    while (cin)
    {
        string line;
        getline(cin, line);
        int pos = 0;
        int ts = line.find("<", pos);
        while(ts != string::npos)
        {
            int te = line.find(">", ts + 1);
            tags.push_back(line.substr(ts, te - ts + 1));
            pos = te + 1;
            ts = line.find("<", pos);
        }
    }
    return tags;
}

bool isHtmlMatched(const vector<string>& tags)
{
    LinkedStack<string> S;
    typedef vector<string>::const_iterator Iter;

    for(Iter p = tags.begin(); p != tags.end(); ++p)
    {
        if(p->at(1) != '/')
            S.push(*p);
        else{
            if(S.empty()) return false;
            string open = S.top().substr(1);
            string close = p->substr(2);
            if(open != close) return false;
            else S.pop();
        }
    }
    if(S.empty()) return true;
    else  return false;
}

int main() {
     // main HTML tester
    if (isHtmlMatched(getHtmlTags())) // get tags and test them
    cout << "The input file is a matched HTML document." << endl;
    else
    cout << "The input file is not a matched HTML document." << endl;
}
