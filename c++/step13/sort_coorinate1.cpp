#include<iostream>
#include<vector>
#include<algorithm>
bool compare(std::pair<int, int> p1, std::pair<int , int> p2){
    if(p1.first == p2.first)
        return p1.second < p2.second;
    else return p1.first < p2.first;
}


int main()
{
    int n;
    std::cin >> n;
    std::vector<std::pair<int, int>> v(n);
    int x, y;
    std::pair<int,int> p;
    for(int i = 0; i < n; i++)
    {
        std::cin >> p.first >> p.second;
        v[i] = (std::make_pair(p.first, p.second));
    }
    
    std::sort(v.begin(), v.end(), compare);
    for(int i = 0; i < n; i++)
        std::cout<<v[i].first <<" "<<v[i].second<<std::endl;
    return 0;
}
