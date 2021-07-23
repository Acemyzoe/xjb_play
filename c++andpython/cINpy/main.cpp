//Python调用C/C++可执行程序
//编译成二进制可执行文件：g++ -o main main.cpp
#include <iostream>  
using namespace std;  
int test()  
{  
    int a = 10, b = 5;  
    return a+b;  
}  

int main()  
{  
    cout<<"---begin---"<<endl;  
    int num = test();  
    cout<<"num="<<num<<endl;  
    cout<<"---end---"<<endl;  
}