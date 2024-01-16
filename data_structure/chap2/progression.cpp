#include<iostream>
using namespace std;

class Progression{
    public:
        Progression(long f = 0)
        : fisrt(f), cur(f){}
        virtual ~Progression(){};
        void printProgression(int n);
    protected:
        virtual long fisrtValue();
        virtual long nextValue();
    protected:
        long fisrt;
        long cur;
};

void Progression::printProgression(int n)
{
    cout<<fisrtValue();
    for(int i = 2; i <=n; i++)
        cout<<' '<<nextValue();
    cout<<endl;
}

long Progression::fisrtValue()
{
    cur = fisrt;
    return cur;
}

long Progression::nextValue(){
    return ++cur;
}

class ArithProgression: public Progression{
    public:
        ArithProgression(long i = 1);
    protected:
        virtual long nextValue();
    protected:
        long inc;
};

ArithProgression::ArithProgression(long i)
    :Progression(),inc(i){}

long ArithProgression::nextValue()
{
    cur+= inc;
    return cur;
}

class GeomProgression: public Progression{
    public:
        GeomProgression(long b = 1);
    protected:
        virtual long nextValue();
    protected:
        long base;
};

GeomProgression::GeomProgression(long b)
    :Progression(1), base(b){}

long GeomProgression::nextValue(){
    cur *= base;
    return cur;
}

class FibonacciProgression: public Progression{
    public:
        FibonacciProgression(long f = 0, long s = 1);
    protected:
        virtual long fisrtValue();
        virtual long nextValue();
    protected:
        long second;
        long prev;
};

FibonacciProgression::FibonacciProgression(long f, long s)
    :Progression(f), second(s), prev(second - fisrt){}

long FibonacciProgression::fisrtValue(){
    cur = fisrt;
    prev = second - fisrt;
    return cur;
}

long FibonacciProgression::nextValue(){
    long temp = prev;
    prev = cur;
    cur += temp;
    return cur;
}


int main() {
    Progression* prog;
    // test ArithProgression
    cout << "Arithmetic progression with default increment:\n";
    prog = new ArithProgression();
    prog->printProgression(10);
    cout << "Arithmetic progression with increment 5:\n";
    prog = new ArithProgression(5);
    prog->printProgression(10);
    // test GeomProgression
    cout << "Geometric progression with default base:\n";
    prog = new GeomProgression();
    prog->printProgression(10);
    cout << "Geometric progression with base 3:\n";
    prog = new GeomProgression(3);
    prog->printProgression(10);
    // test FibonacciProgression
    cout << "Fibonacci progression with default start values:\n";
    prog = new FibonacciProgression();
    prog->printProgression(10);
    cout << "Fibonacci progression with start values 4 and 6:\n";
    prog = new FibonacciProgression(4, 6);
    prog->printProgression(10);
    return 0; // successful execution
}