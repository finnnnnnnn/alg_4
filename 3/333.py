import time
from collections import deque

time_start = time.perf_counter()

open_sc = ['[', '(']
close_sc = [']', ')']

f = open('input.txt')
num = []
stack = deque()
while True:
    l = f.readline()
    if not l:
        break
    num.append(l.split())

def check(str_):
    stack = []
    for i in str_:
        if i in open_sc:
            stack.append(i)
        elif i in close_sc:
            p = close_sc.index(i)
            if (len(stack) > 0) and (open_sc[p] == stack[len(stack) - 1]):
                stack.pop()
            else:
                return 'NO'
    if len(stack) == 0:
        return 'YES'
    else:
        return 'NO'

o = open('output.txt', 'w')

for i in range(1, len(num)):
    if check(str(num[i])) == 'YES':
        o.write('YES \n')
    if check(str(num[i])) == 'NO':
        o.write('NO \n')

# print('used memory:', (process.memory_info().rss / 1024 / 1024), 'Mbytes')
print("time passed: %s seconds " % (time.perf_counter() - time_start))

