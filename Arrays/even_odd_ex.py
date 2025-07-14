# Suppose your input is an array of integers and you have to reorder the entries such that even entries appear first
# There is a brute force solution that used O(n) space but we can do it with O(1) space
def even_odd(A):
    next_even, next_odd = 0, len(A)-1
    while next_even < next_odd:
        if A[next_even] % 2 == 0:
            next_even += 1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1
    return A

B = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(even_odd(B))

# Variation: How can we do this so that odd entries appear first?

def odd_even(A):
    next_odd, next_even = 0, len(A) - 1
    while next_odd < next_even:
        if A[next_odd] % 2 == 1:
            next_odd += 1
        else:
            A[next_odd], A[next_even] = A[next_even], A[next_odd]
            next_even -= 1
    return A

print(odd_even(B))