# Find the first non-repeating character and return its index else -1
def firstUniqChar(s):
    queue = []
    for i in s:
        if len(queue) == 0:
            queue.append(i)
        elif i == queue[0]:
            queue.pop(0)
        else:
            queue.append(i)
    if len(queue) == 0:
        return -1
    else:
        return list(s).index(queue[0])

print(firstUniqChar("aadadaad"))