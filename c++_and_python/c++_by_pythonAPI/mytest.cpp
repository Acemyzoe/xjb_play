// g++ demo.cpp -I/usr/include/python3.8 -lpython3.8
// g++ demo.cpp `pkg-config python3-embed --libs --cflags` -o demo
#include "Python.h"
using namespace std;

int main()
{
    Py_Initialize();              //初始化，创建一个Python虚拟环境
    if (Py_IsInitialized())
    {
        PyObject* pModule = NULL;
        PyObject* pFunc = NULL;
        PyRun_SimpleString("import sys");
        PyRun_SimpleString("sys.path.append('./')");
        pModule = PyImport_ImportModule("mytest");  //参数为Python脚本的文件名
        if (pModule)
        {
            pFunc = PyObject_GetAttrString(pModule, "hehe");   //获取函数
            PyEval_CallObject(pFunc, NULL);           //执行函数
        }
        else
        {
            printf("导入Python模块失败...\n");
        }
    }
    else
    {
        printf("Python环境初始化失败...\n");
    }
    Py_Finalize();
}
