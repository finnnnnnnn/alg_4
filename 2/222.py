import time

time_start = time.perf_counter()

class node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
    def __str__(self):
        return str(self.value)

class queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def pop(self):
        if self.head:
            host = self.head
            self.head = self.head.next
            return host

    def push(self, value):
        n = node(value)
        if self.head == None:
            self.head = n
            self.tail = n
            return None
        self.tail.next = n
        self.tail = n

if __name__ == '__main__':
    mas = []
    que = queue()
    with open('input.txt') as f:
        while True:
            l = f.readline()
            if not l:
                break
            mas.append(l.split())

    with open('output.txt', 'w') as o:
        for i in range(5):
            if mas[i][0] == '+':
                que.push(mas[i][1])
            elif mas[i][0] == '-':
                o.write(f'{que.pop()}\n')

# print('used memory:', (process.memory_info().rss / 1024 / 1024), 'Mbytes')
print("time passed: %s seconds " % (time.perf_counter() - time_start))