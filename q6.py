# Q6 - Recursion and Its Limits

calls = 0

def ways_naive(n):
    global calls
    calls += 1

    if n <= 1:
        return 1

    return ways_naive(n - 1) + ways_naive(n - 2)


print("Naive Recursion:")
calls = 0
print("Ways:", ways_naive(5))
print("Function Calls:", calls)
from functools import lru_cache

@lru_cache(maxsize=None)
def ways_memo(n):
    global calls
    calls += 1

    if n <= 1:
        return 1

    return ways_memo(n - 1) + ways_memo(n - 2)


print("\nMemoised Recursion:")
calls = 0
print("Ways:", ways_memo(5))
print("Function Calls:", calls)
print("\nVerification from n = 1 to 6:")

for n in range(1, 7):
    print("n =", n, "Ways =", ways_memo(n))
    print("\nFunction Call Comparison:")

for n in [10, 20, 25, 30]:
    calls = 0
    ways_naive(n)
    naive_calls = calls

    calls = 0
    ways_memo.cache_clear()
    ways_memo(n)
    memo_calls = calls

    print("n =", n)
    print("Naive Calls:", naive_calls)
    print("Memoised Calls:", memo_calls)
    import sys

print("\nRecursion Limit:")
print("Current Limit:", sys.getrecursionlimit())

ways_memo.cache_clear()

try:
    print("Ways for 1000 steps:", ways_memo(1000))
except RecursionError:
    print("RecursionError: Maximum recursion depth exceeded")
def ways_loop(n):
    if n <= 1:
        return 1

    a = 1
    b = 1

    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c

    return b


print("\nIterative Solution:")
print("Ways for 1000 steps:", ways_loop(1000))   
# Recursion Call Tree for n = 5
#
#                  ways(5)
#                /        \
#           ways(4)      ways(3)
#           /    \       /    \
#       ways(3) ways(2) ways(2) ways(1)
#        /  \
#    ways(2) ways(1)
#
# Repeated calls occur for ways(3) and ways(2).
# Memoisation stores results and avoids repeated calculations.
print("\nTime and Space Complexity:")
print("Naive Recursion: Time O(2^n), Space O(n)")
print("Memoised Recursion: Time O(n), Space O(n)")
print("Iterative Method: Time O(n), Space O(1)")