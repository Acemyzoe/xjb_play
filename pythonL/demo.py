"""
runing 100
"""
import time
# from time import clock
import argparse
from multiprocessing import Process
from multiprocessing import cpu_count
import random

def exec_func(bt):
    while True: 
        for i in range(0, 100):
            pass
        time.sleep(bt)

def test():

    parse = argparse.ArgumentParser(description='runing')
    parse.add_argument(
        "-c",
        "--count",
        default= cpu_count(),
        help='cpu count'
        )
    parse.add_argument(
        "-t",
        "--time",
        default= 0.01,
        help='cpu time'
        )

    args = parse.parse_args()
    cpu_logical_count = int(args.count)
    cpu_sleep_time = args.time

    try:
        cpu_sleep_time = int(args.time)
    except ValueError:
        try:
            cpu_sleep_time = float(args.time)
        except ValueError as ex:
            raise ValueError(ex)

    print('\n====================占用CPU核数{}.===================='.format(cpu_logical_count))
    print('\n资源浪费starting......')
    print(cpu_sleep_time)

    try:
        p = Process(target=exec_func, args=("bt",))
        ps_list = []
        for i in range(0, cpu_logical_count):
            ps_list.append(Process(target=exec_func, args=(cpu_sleep_time,)))
        for p in ps_list:
            p.start()
        for p in ps_list:
            p.join()
    except KeyboardInterrupt:
        print("手工结束!")

def test2(n):
    l = [random.random() for i in range(n)]
    l.sort()
    return l 

if __name__ == "__main__":
    test2(2000)