import threading
import time


class MyThread(threading.Thread):
    def __init__(self,name):
        super().__init__()
        self.name = name

    def run(self):
        for i in range(10):
            print(self.name)
            time.sleep(.5)

t1 = MyThread('ali')
t2 = MyThread('mamad')

t1.start()
t2.start()

t1.join()
t2.join()