import threading
import time

class CountdownTime(threading.Thread):
  def __init__(self, name, count):
    threading.Thread.__init__(self)
    self.count = count
    self.name = name

  def run(self):
    while self.count > 0:
      print(f"{self.name} Odliczam {self.count}")
      self.count -= 1
      time.sleep(1)
    return

t1 = CountdownTime("A", 10)
t2 = CountdownTime("B", 20)

t1.start()
t2.start()