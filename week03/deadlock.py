import threading
from time import sleep
import os, random

# 设置为2更容易重现死锁, 这种是每次
numPhilosophers = numForks = 3


class Philosopher(threading.Thread):
    def __init__(self, index):
        threading.Thread.__init__(self)
        self.index = index
        self.leftFork = forks[self.index]
        self.rightFork = forks[(self.index + 1) % numForks]

    def run(self):
        while True:

            self.leftFork.pickup()
            self.rightFork.pickup()
            #sleep(random.uniform(1, 3) / 1000)  #

            self.dining()


            self.leftFork.putdown()
            #print(self.index, 1, 2)
            self.rightFork.putdown()
            #print(self.index, 2, 2)
            self.thinking()

    def dining(self):
        # print(self.index,self.leftFork.index,self.rightFork.index)
         print("Philosopher", self.index, " starts to eat.")
         print(self.index, 0, 3)
         sleep(random.uniform(1, 3) / 1000) #
         print("Philosopher", self.index, " finishes eating and leaves to think.")

         #print('\n')
        #sleep(2) #random.uniform(1, 3) / 1000

    def thinking(self):
        sleep(random.uniform(1, 3) / 1000)


class Fork():
    def __init__(self, index):
        self.index = index
        self._lock = threading.Lock()


    def pickup(self):

        self._lock.acquire()

    def putdown(self):
        self._lock.release()
#timeout=random.uniform(1, 3) / 1000

if __name__ == '__main__':
    # 创建叉子与哲学家实例
    forks = [Fork(idx) for idx in range(numForks)]
    philosophers = [Philosopher(idx) for idx in range(numPhilosophers)]

    # 开启所有的哲学家线程
    for philosopher in philosophers:
        philosopher.start()

    try:  # 异常处理语句，检测try后语句是否正常
        while True: sleep(0.1)
    except Exception as e:
        raise e
