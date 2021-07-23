//Python调用C库比较简单，不经过任何封装打包成so，再使用python的ctypes调用即可。
//gcc编译生成动态库libpycall.so：gcc -o libpycall.so -shared -fPIC pycall.c
//使用g++编译生成C动态库的代码中的函数或者方法时，需要使用extern "C"来进行编译。
#include <stdio.h>  
#include <stdlib.h>  
int foo(int a, int b)  
{  
  printf("input %d and %d\n", a, b);  
  printf("output %d \n", a+b);  
  return a+b;  
}