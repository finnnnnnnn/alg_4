import time
from random import randint

time_start = time.perf_counter()

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
    def __str__(self):
        return str(self.value)

class queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.mid = None
        self.length = 0

    def pop(self):
        if not self.head:
            pass
        host = self.head
        self.head = self.head.next
        if self.length % 2 == 0:
            self.mid = self.mid.next
        self.length -= 1
        return host

    def push(self, value):
        n = Node(value)
        if self.head == None:
            self.head = n
            self.mid = n
            self.tail = n
            self.length += 1
            return None
        self.tail.next = n
        self.tail = n
        if self.length % 2 == 0:
            self.mid = self.mid.next
        self.length += 1

    def mid_push(self, value):
        n = Node(value)
        if self.head == None:
            self.head = n
            self.mid = n
            self.tail = n
            self.length += 1
            return None
        n.next = self.mid.next
        self.mid.next = n
        if self.length % 2 == 0:
            self.mid = self.mid.next
        self.length += 1

if __name__ == "__main__":
    mas = []
    que = queue()
    with open('input.txt') as f:
        while True:
            l = f.readline()
            if not l:
                break
            mas.append(l.split())
    with open('output.txt', 'w') as o:
        for i in range(int(mas[0][0]) + 1):
            if mas[i][0] == '+':
                que.push(mas[i][1])
            elif mas[i][0] == '*':
                que.mid.push(mas[i][1])
            elif mas[i][0] == '-':
                o.write(f"{que.pop()}\n")

# print('used memory:', (process.memory_info().rss / 1024 / 1024), 'Mbytes')
print("time passed: %s seconds " % (time.perf_counter() - time_start))