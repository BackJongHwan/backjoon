#include<iostream>

int main()
{
    std::ios_base::sync_with_stdio(false);
    int n , a, b;
    std::cin.tie(NULL);
    std::cin >> n;
    for(int i = 0; i < n; i++)
    {
        std::cin >> a >> b;
        std::cout << a + b<<"\n";
    }
    
}
