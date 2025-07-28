# Realized I had already solved this problem
def groupAnagrams(strs):
    hashmap = {}
    for i in strs:
        if ''.join(sorted(i)) not in hashmap:
            hashmap[''.join(sorted(i))] = [i]
        else:
            hashmap[''.join(sorted(i))].append(i)
    output = []
    for j in hashmap.keys():
        output.append(hashmap[j])
    return output