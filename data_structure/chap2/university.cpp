#include<iostream>
#include<string>
using namespace std;
class Person{
    private:
        string name;
        string idNum;
    public:
        Person();
        Person(const string &name, const string &id);
        void print();
        string getName();

};

void Person::print()
{
    cout<<"Name "<< name<<endl;
    cout<<"IDnum "<< idNum<<endl;
}

string Person::getName()
{
    return this->name;
}

Person::Person(const string &name, const string &id)
    :
        name(name), idNum(id)
        {
        }


class Student: public Person{
    private:
        string major;
        int gradYear;
    public:
        Student();
        Student(const string &name, const string &id, const string &major, int gradYear);
        void print();
        void changeMajor(const string & newMajor);
};

void Student::print()
{
    Person::print();
    cout<<"Major "<<major<<endl;
    cout<<"Year "<<gradYear<<endl;
}

Student::Student(const string &name, const string &id, const string &major, int gradYear)
:
    Person(name, id), major(major), gradYear(gradYear)
    {}

void Student::changeMajor(const string &newMajor)
{
    this->major = newMajor;
}

int main()
{
    Person person("Mary", "12-345");
    Student student("Bob", "98-764", "Math", 2012);
    cout<<student.getName()<<endl;
    person.print();
    student.print();
    //person.changeMajor(""
    student.changeMajor("English");
    return 0;
}
