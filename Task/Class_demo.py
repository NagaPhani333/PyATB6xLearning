import math

count = 0

class Increment:
    count1 = 1
    def add(self):
        count2 = 3
        def add1():
            count3 = 4
            global count4
            count4 = 5
            print(count4)
            print(count3)
            print(count2)
            print(self.count1)
            print(count)
        add1()
        print(count4)
call_incr = Increment()
call_incr.add()