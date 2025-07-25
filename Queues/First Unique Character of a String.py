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

# Hash Table Approach
def firstUniqCharHash(s):
    queue = {}
    for c in list(s):
        if c not in queue.keys():
            queue.update([(c, 1)])
            continue
        else:
            queue[c] += 1
    for i, c in enumerate(s):
        if queue[c] == 1:
            return i
    return -1

print(firstUniqChar("aadadaad"))
print(firstUniqCharHash("aadadaad"))