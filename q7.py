# Q7 - Diagnose, Redesign and Validate

calls = 0

def ways_original(n):
    global calls
    calls += 1

    if n <= 1:
        return 1

    return ways_original(n - 1) + ways_original(n - 2)


print("Original Recursive Method:")

for n in [10, 20, 25, 30]:
    calls = 0
    result = ways_original(n)

    print("n =", n)
    print("Ways:", result)
    print("Function Calls:", calls)
    from functools import lru_cache

memo_calls = 0

@lru_cache(maxsize=None)
def ways_redesigned(n):
    global memo_calls
    memo_calls += 1

    if n <= 1:
        return 1

    return ways_redesigned(n - 1) + ways_redesigned(n - 2)


print("\nRedesigned Memoised Method:")

for n in [10, 20, 25, 30]:
    memo_calls = 0
    ways_redesigned.cache_clear()

    result = ways_redesigned(n)

    print("n =", n)
    print("Ways:", result)
    print("Function Calls:", memo_calls)
    import time

n = 30

print("\nExecution Time Comparison:")

start = time.perf_counter()
ways_original(n)
original_time = time.perf_counter() - start

ways_redesigned.cache_clear()
start = time.perf_counter()
ways_redesigned(n)
redesigned_time = time.perf_counter() - start

print("Original Time:", original_time, "seconds")
print("Redesigned Time:", redesigned_time, "seconds")
print("\nValidation:")

for n in [1, 2, 3, 4, 5, 10, 20, 25, 30]:
    original = ways_original(n)

    ways_redesigned.cache_clear()
    redesigned = ways_redesigned(n)

    if original == redesigned:
        print("n =", n, "Both results match")
    else:
        print("n =", n, "Results do not match")
        print("\nDiagnosis:")
print("Original recursion repeats the same calculations.")
print("The number of function calls increases exponentially.")
print("For n = 30, original method uses 2692537 calls.")
print("Memoisation stores already calculated results.")

print("\nDesign Objective:")
print("Reduce function calls while getting the same result.")

print("\nDesign Changes:")
print("Used memoisation to store previous results.")
print("Extra memory is required to store calculated results.")

print("\nPrediction:")
print("Memoisation will reduce execution time and function calls.")

print("\nFinal Decision:")
print("Memoisation is better for larger inputs.")
print("Original recursion is simpler for very small inputs.")
print("\nPseudocode:")
print("1. Start")
print("2. Read number of steps n")
print("3. Check whether result is already stored")
print("4. If stored, return the result")
print("5. Otherwise, calculate ways(n-1) + ways(n-2)")
print("6. Store the calculated result")
print("7. Return the result")
print("8. Stop")
print("\nFinal Comparison:")
print("Input n = 30")
print("Original Function Calls: 2692537")
print("Memoised Function Calls: 31")
print("Both methods produce the same result: 1346269")
print("Memoisation avoids repeated calculations.")