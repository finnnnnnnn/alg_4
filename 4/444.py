import time

time_start = time.perf_counter()

f = open('input.txt', 'r')
s = f.readline()
f.close()
stack = []
bracket = {')': '(', '}': '{', ']': '['}

f = open('output.txt', 'w')

for i in range(len(s)):
    el = s[i]
    if el == '(' or el == '[' or el == '{':
        stack += [(el, i)]
    elif el == ')' or el == ']' or el == '}':
        if len(stack) == 0 or bracket[el] != stack[-1][0]:
            f.write(str(i + 1))
            exit(0)
        stack.pop()

if len(stack) != 0:
    f.write(str(stack[0][1] + 1))
else:
    f.write('Success')

f.close()

# print('used memory:', (process.memory_info().rss / 1024 / 1024), 'Mbytes')
print("time passed: %s seconds " % (time.perf_counter() - time_start))