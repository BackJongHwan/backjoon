#include<iostream>

int main()
{
    int m, n;
    std::cin >> m >> n;
    int **a = new int*[m];
    int **b = new int*[m];

    for(int i = 0; i < m; i++)
    {
        a[i] = new int[n];
        b[i] = new int[n];
    }
    


    for(int i = 0; i < m; i++)
    {
        for(int j = 0; j < n; j++)
        {
            std::cin>> a[i][j];
        }
    }

    for(int i = 0; i < m; i++)
    {
        for(int j = 0; j < n; j++)
        {
            std::cin>> b[i][j];
            a[i][j] += b[i][j];
        }
    }

    for(int i = 0; i < m; i++)
    {
        for(int j = 0; j < n; j++)
        {
            std::cout<<a[i][j]<<" ";
        }
        std::cout<< '\n';
    }
    
    for(int i = 0; i < m; i++)
    {
        delete a[i];
        delete b[i];
    }
    delete []a;
    delete []b;


}
