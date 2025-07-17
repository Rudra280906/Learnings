# Write a program that takes an array A and an index i into A and rearranges the elements s.t. 
# all elements less than A[i] appear first, followed by equal to, and the greater
def dutch_national_flag_1(A, i):
    less = []
    equal = []
    greater = []
    target = A[i]
    for j in A:
        if j < target:
            less.append(j)
        elif j == target:
            equal.append(j)
        else:
            greater.append(j)
    for k in equal:
        less.append(k)
    for k in greater:
        less.append(k)
    return less

def dutch_national_flag_2(A, i):
    pivot = A[i]
    small = 0
    for j in range(len(A)):
        if A[j] < pivot:
            A[j], A[small] = A[small], A[j]
            small += 1
    larger = len(A) - 1
    for j in reversed(range(len(A))):
        if A[j] > pivot:
            A[j], A[larger] = A[larger], A[j]
            larger -= 1
    return A

print(dutch_national_flag_2([0, 1, 2, 0, 2, 1, 1], 2))