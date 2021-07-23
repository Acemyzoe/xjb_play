
#include "python3.8/Python.h"
#include <iostream>
using namespace std;

int predict();

int main()
{
    cout << predict() << endl;
}


int predict()
/************************************************* 
Description:    预测用户负荷
Input:          NULL 
Output:         (int)预测值 
*************************************************/ 
{
	Py_Initialize();
	if( !Py_IsInitialized()){
		cout << "python init fail" << endl;
		return 0;
	}
	PyRun_SimpleString("import sys");
	PyRun_SimpleString("sys.path.append('./')");

	PyObject* pModule = PyImport_ImportModule("lstm_model");
	if( pModule == NULL ){
		cout <<"[Error] module not found" << endl;
		return -1;
	}
	//模块的字典列表
	PyObject* pDict = PyModule_GetDict(pModule);
	PyObject *pClass = PyDict_GetItemString(pDict,"Lstm_Model"); 
    if (pClass == NULL){
        cout << "[Error] import class error" << endl;
        return -1;
    }
	//得到构造函数而不是类实例
    PyObject* pConstruct = PyInstanceMethod_New(pClass);
	//实例化类得到类对象
	PyObject *pInstance = PyObject_CallObject(pConstruct,NULL);
	if (pInstance == NULL){
        cout << "[Error] instance error" << endl;
        return -1;
    }
	//调用对象的成员函数
	PyObject* pRet = PyObject_CallMethod(pInstance,"lstm_predict","s","./lstmMODEL/10_26.h5");
	if (pRet == NULL){
		cout << "[Error] function error" << endl;
		return -1;
    }
	//写回C++变量
	int res ;
	PyArg_Parse(pRet,"i", &res);

	Py_DECREF(pModule);
    Py_DECREF(pClass);
    Py_DECREF(pInstance);
    Py_DECREF(pRet);
	Py_Finalize();

	return res;
}