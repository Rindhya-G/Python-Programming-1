def count_strings(n):
    arr= [[0] * 5 for _ in range(n + 1)]
    for j in range(5):
        arr[1][j] = 1
    for i in range(2, n + 1):
        for j in range(5):
            arr[i][j] = sum(arr[i - 1][k] for k in range(j + 1))
    total_count = sum(arr[n])
    return total_count
n = 2
result = count_strings(n)
print(f"The number of lexicographically sorted vowel strings of length {n} is: {result}")
