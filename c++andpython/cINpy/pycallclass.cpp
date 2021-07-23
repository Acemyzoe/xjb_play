/*
Python调用C++(类)动态链接库 
需要extern "C"来辅助，也就是说还是只能调用C函数，不能直接调用方法，但是能解析C++方法。
不是用extern "C"，构建后的动态链接库没有这些函数的符号表。
g++编译生成动态库libpycall.so：g++ -o libpycallclass.so -shared -fPIC pycallclass.cpp
*/
#include <iostream>  
using namespace std;  
  
class TestLib  
{  
    public:  
        void display();  
        void display(int a);  
};

void TestLib::display() {  
    cout<<"First display"<<endl;  
}  
  
void TestLib::display(int a) {  
    cout<<"Second display:"<<a<<endl;  
}  

extern "C" {  
    TestLib obj;  
    void display() {  
        obj.display();   
      }  
    void display_int() {  
        obj.display(1);   
      }  
}