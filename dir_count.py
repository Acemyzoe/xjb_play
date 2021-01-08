
import os

def isnothide(dir):
    '隐藏文件判断'
    dir = str(dir).split("/")[-1]
    if str(dir).startswith("."):
        return False
    else: return True

def total_dir_count(dir):
    '计算文件(夹)总容量'
    total_dir = float(0)
    #判断文件还是文件夹
    #如果是文件，直接进行统计
    if os.path.isfile(dir) and isnothide(dir):
        if os.path.getsize(dir)>100*1024*1024:
            print(dir+"----",os.path.getsize(dir)/float(1024*1024))
        total_dir += os.path.getsize(dir)/float(1024*1024)
    #如果是文件夹，需要重复调用遍历再判断文件还是文件夹进行统计
    if os.path.isdir(dir) and isnothide(dir):
        # dlist获取所有文件信息
        dlist = os.listdir(dir)
        #遍历所有文件，赋值到box变量中
        for x in dlist:
            box = os.path.join (dir, x)
            if os.path.isdir(box) and isnothide(box):
                #递归调用一下
                total_dir += total_dir_count(box)
            if os.path.isfile(box) and isnothide(box):
                if os.path.getsize(box)>100*1024*1024:
                    print(box+"----",os.path.getsize(box)/float(1024*1024))
                total_dir += os.path.getsize(box)/float(1024*1024)
    return total_dir

if __name__ == "__main__":
    # import timeit
    # print(timeit.timeit("demo()",setup="from __main__ import demo",number=1000))
    # print(total_dir_count("/home/ace/Desktop/github/data_anasylsis"))
    print(total_dir_count("/home/ace/Downloads"))