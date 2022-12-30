import time
from collections import deque

time_start = time.perf_counter()

f = open("input.txt")
stack = deque()
removed = []
a = []

while True:
    l = f.readline()
    if not l:
        break
    a.append((l.split()))

for i in range(len(a)):
    if a[i][0] == '+':
        stack.append(a[i][1])
    elif a[i][0] == '-':
        removed.append(str(stack[-1]))
        stack.pop()

o = open('output.txt', 'w')
o.write(' '.join(str(i) for i in removed))
o.close()

# print('used memory:', (process.memory_info().rss / 1024 / 1024), 'Mbytes')
print("time passed: %s seconds " % (time.perf_counter() - time_start))