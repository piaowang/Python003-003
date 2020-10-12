# 实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。

import datetime


def timer(func):
    def wrapper(*args, **kwargs):
        starttime = datetime.datetime.now()
        print(f'开始时间{starttime}')
        func(*args, **kwargs)
        endtime = datetime.datetime.now()
        print(f'开始时间{endtime}')
        print(f'耗时{(endtime - starttime).seconds}')

    return wrapper


@timer
def run_for(*args, **kwargs):
    for i in range(10000000):
        a = i + 1
        # print(a)
    for i in args:
        print(args)
    print(kwargs)
    for pet, name in kwargs.items():
        print(f"{pet}:{name}")

a = run_for('xzxz','vs', a= 7, b=3, d= 90)
