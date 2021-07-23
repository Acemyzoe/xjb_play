#include <stdlib.h>
using namespace std;

int main ()
{
  system("python -c 'from mytest import add; print(add(1,2))'"); //system()在命令执行完之前是会阻塞主进程
  //system("./demo2");
  return 0;
}
