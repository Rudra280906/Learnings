# Find the first non-repeating character and return its index else -1
def firstUniqChar(s):
    queue = []
    queue2 = []
    for i in s:
        if len(queue) == 0:
            queue.append(i)
            continue
        elif i == queue[0]:
            queue.pop(0)
            queue2.append(i)
        else:
            queue.append(i)
    if len(queue) == 0:
        return -1
    for i in queue2:
        if i in queue:
            queue.remove(i)
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

print(firstUniqChar("aadaadad"))
print(firstUniqCharHash("aadaadad"))
print(firstUniqChar("aaad"))
print(firstUniqCharHash("aaad"))