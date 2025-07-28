#Already did this problem
#First Approach
def lengthOfLongestSubstring(s: str) -> int:
    if s == "":
        return 0
    max_start = [1 for k in s]
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[j] in s[i:j]:
                break
            else:
                max_start[i] += 1
    return max(max_start)


#Optimized Approach
#This was found online after doing the first approach, I do not understand it
def lengthOfLongestSubstring2(s: str) -> int:
    p1, p2 = 0, 0
    chars = set([])
    maxlen = 0

    while p2 < len(s):
        c = s[p2]
        while c in chars:
            chars.remove(s[p1])
            p1 += 1
        chars.add(c)
        maxlen = max(maxlen, p2-p1+1)
        p2 += 1
    return maxlen