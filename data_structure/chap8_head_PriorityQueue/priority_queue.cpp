#include<iostream>
#include<queue>
#include<vector>
typedef double E;
class Point2D{
public:
    Point2D(E x, E y)
        :x(x), y(y){}
    E& getX() const{
        return x;
    }
    E& getY() const{
        return y;
    }
private:
    E x, y;
};

class LeftRight{
public:
    bool operator()(const Point2D& p, const Point2D& q) const
    {   return p.getX() < q.getX();}
};

class BottomTop{
public:
    bool operator()(const Point2D& p, const Point2D& q) const
    {   return p.getY() < q.getY(); }
};
int main()
{
    std::priority_queue<int> p1;
    std::priority_queue<Point2D, std::vector<Point2D>, LeftRight> p2;

    p2.push(Point2D(8.5, 4.6));
    p2.push(Point2D(1.3, 5.7));
    p2.push(Point2D(2.5, 0.6));
    std::cout<<p2.top()<<std::endl; p2.pop();
    std::cout<<p2.top()<<std::endl; p2.pop();
    std::cout<<p2.top()<<std::endl; p2.pop();

    return 0;
}