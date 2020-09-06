# 示例代码
import threading
import os, random
from time import sleep

log = []
inter = 0

class DiningPhilosophers(threading.Thread):
    def __init__(self, index,num):
        threading.Thread.__init__(self)
        self.num = num
        self.index = index
        self.leftFork = forks[self.index]  # 分配叉子的序号
        self.rightFork = forks[(self.index + 1) % numForks]  # 右边叉子的序号如下

    def run(self):
        global inter
        #print(self.num)
        while True:
            self.leftFork.pickLeftFork()
            self.rightFork.pickRightFork()
            self.eat()
            self.leftFork.putLeftFork()
            self.rightFork.putLeftFork()
            sleep(random.uniform(1, 3) / 1000)
            if (inter > self.num*5-1):
                break

    def eat(self):
        global inter
        global log
        # print("Philosopher", self.index, " starts to eat.")
        inter += 1
        print(inter)
        log_ok = [self.index, 0, 3]
        #print(log_ok)
        log.append(log_ok)
        sleep(random.uniform(1, 3) / 1000)

        # print("Philosopher", self.index, " finishes eating and leaves to think.")


class Fork():
    def __init__(self, index):
        self.index = index
        self._lock = threading.Lock()

    def pickLeftFork(self):
        self._lock.acquire(timeout=5)
        log_ok = [self.index, 1, 1]
        # print(log_ok)
        log.append(log_ok)

    def pickRightFork(self):
        self._lock.acquire(timeout=5)
        log_ok = [self.index, 2, 1]
        #print(log_ok)
        log.append(log_ok)

    def putLeftFork(self):
        self._lock.release()
        log_ok = [self.index, 1, 2]
        #print(log_ok)
        log.append(log_ok)
    def putRightFork(self):
        self._lock.release()
        log_ok = [self.index, 2, 2]
        #print(log_ok)
        log.append(log_ok)

def wantsToEat(num):
    philosopher = 5  # 五个哲学家
    philosophers = [DiningPhilosophers(idx,num) for idx in range(philosopher)]
    
    # 开启所有的哲学家线程
    for philosopher in philosophers:
        philosopher.start()
    philosopher.join()

    print(log)
    #philosopher.terminate()
    try:  # 异常处理语句，检测try后语句是否正常
        while True: sleep(0.1)
    except Exception as e:
        raise e


if __name__ == '__main__':
    numForks = 5  # 五个叉子，相当于有五个锁，能占有对应左右两个就能吃东西
    forks = [Fork(idx) for idx in range(numForks)]
    wantsToEat(2)  ## 进行多少次查找


