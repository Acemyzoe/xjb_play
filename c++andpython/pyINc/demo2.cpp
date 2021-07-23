//////通过在c++代码中加载python模块的方式
// 编译命令一：g++ demo2.cpp -I/usr/include/python3.8 -lpython3.8 -o demo2
// 编译命令二：g++ demo2.cpp `pkg-config python3-embed --libs --cflags` -o demo2
#include <python3.8/Python.h>
#include <iostream>
using namespace std;

int add(int num1,int num2);

int main()
{
    int i = 10;
    int j = 20;
    cout << add(i,j) << endl;
}

int add(int num1,int num2)
{
	Py_Initialize();
	if( !Py_IsInitialized()){
		cout << "python init fail" << endl;
		return 0;
	}
	PyRun_SimpleString("import sys");
	PyRun_SimpleString("sys.path.append('./')");

	PyObject* pModule = PyImport_ImportModule("mytest");
	if( pModule == NULL ){
		cout <<"module not found" << endl;
		return 1;
	}

	PyObject* pFunc = PyObject_GetAttrString(pModule, "add");
	if( !pFunc || !PyCallable_Check(pFunc)){
		cout <<"not found function add" << endl;
		return 0;
	}

	PyObject* args = Py_BuildValue("(ii)", num1, num2);
	PyObject* pRet = PyObject_CallObject(pFunc, args );
    Py_DECREF(args);

	int res = 0;
	PyArg_Parse(pRet, "i", &res );
    Py_DECREF(pRet);

	Py_Finalize();

	return res;
}