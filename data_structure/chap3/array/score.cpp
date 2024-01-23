#include<iostream>
using namespace std;

class IndexOutOfBounds {
public:
    IndexOutOfBounds(const string &msg) : message(msg) {}
    string getMessage() const { return message; }

private:
    string message;
};

class GameEntry{
    public:
        GameEntry(const string &n="", int s = 0);
        string getName()const;
        int getScore()const;
        void show()const;
    private:
        string name;
        int score;
};

GameEntry::GameEntry(const string &n, int s)
    :name(n), score(s){}

string GameEntry::getName()const{ return name;}
int GameEntry::getScore() const {return score;}
void GameEntry::show() const
{
    cout<<name<<" "<<score<<endl;
}

class Scores{
    public:
        Scores(int maxEnt = 10);
        ~Scores();
        void add(const GameEntry & e);
        GameEntry remove(int i);
        void show();
    private:
        int maxEntries;
        int numEntries;
        GameEntry *entries;
};

Scores::Scores(int maxEnt){
    maxEntries = maxEnt;
    entries = new GameEntry[maxEntries];
    numEntries = 0;
}

Scores::~Scores(){
    delete [] entries;
}

void Scores::add(const GameEntry &e)
{
    if(numEntries == maxEntries)
    {
        if(e.getScore() < entries[maxEntries -1].getScore())
            return;
    }
    else numEntries++;

    int index = 0;
    while(e.getScore() <= entries[index].getScore() && index < numEntries - 1)
        index++;

    if(index == numEntries -1) 
        entries[index] = e;
    else{
        for(int i = numEntries - 2; i > index - 1; i--)
        {
            entries[i + 1]  = entries[i];
        }
        entries[index] = e;
    }
}

GameEntry Scores::remove(int i) 
{
    if(i < 0 || i >= numEntries)
        throw IndexOutOfBounds("invaild index!");
    GameEntry e = entries[i];
    for(int j = i + 1; j < numEntries; j++)
    {
        entries[j] = entries[j+1];
    }
    numEntries--;
    return e;
}


void Scores::show()
{
    for(int i = 0; i < numEntries; i++)
    {
        cout<<"name, score: "<<entries[i].getName()<<", "<<entries[i].getScore()<<endl;
    }
}

int main()
{
    Scores *board = new Scores();
    GameEntry *a = new GameEntry("john" , 5);
    GameEntry *b = new GameEntry("mary" , 2);
    GameEntry *c = new GameEntry("dndn" , 1231);
    GameEntry *d = new GameEntry("4hj" , 1111);
    GameEntry *e= new GameEntry("number5" , 23);
    board->add(*a);
    board->show();
    board->add(*e);
    board->show();

    board->add(*c);
    board->show();
    board->add(*d);
    board->show();

    board->add(*b);
    board->show();

    GameEntry remove =    board->remove(2);
    remove.show();
    board->show();
    delete board;
    return 0;
}