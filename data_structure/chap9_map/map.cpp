#include<iostream>
#include<map>
#include<string>
int main(){
    std::map<std::string, int> myMap;
    std::map<std::string, int>::iterator p;
    myMap.insert(std::pair<std::string, int>("Rob", 28));
    myMap["Joe"] = 38;
    myMap["Joe"] = 50;
    myMap["Sue"] = 75;
    p = myMap.find("Joe");
    myMap.erase(p);
    myMap.erase("Sue");
    p = myMap.find("Rob");
    if(p == myMap.end()) std::cout<<"nonexistent\n";

    for(p = myMap.begin(); p != myMap.end(); ++p)
    {
        std::cout<<"("<<p->first<<","<<p->second<<")"<<'\n';
    }

    return 0;
}