import time
from random import randint

time_start = time.perf_counter()

f = open('input.txt')
d = [el.replace('\n', '') for el in f.readlines()]
print(d)
mas = []
o = open('output.txt', 'w')

for cmd in d:
    if cmd[0] == '+':
        mas.append(int(cmd[2:]))
    elif cmd == '-':
        del mas[0]
    elif cmd == '?':
        a = 10**9 + 1
        for i in mas:
            if i < a:
                a = i
        print(a, file=o)

# print('used memory:', (process.memory_info().rss / 1024 / 1024), 'Mbytes')
print("time passed: %s seconds " % (time.perf_counter() - time_start))