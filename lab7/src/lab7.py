def naive_search(haystack: str, needle: str):
    n = len(haystack)
    m = len(needle)

    if m == 0:
        return -1, 0

    comparisons = 0
    last_index = -1

    for i in range(n - m + 1):
        match = True
        for j in range(m):
            comparisons += 1
            if haystack[i + j] != needle[j]:
                match = False
                break
        if match:
            last_index = i + m - 1

    return last_index, comparisons

haystack = input("Введіть рядок (haystack): ")
needle = input("Введіть підрядок (needle): ")

index, comparisons = naive_search(haystack, needle)

print(f"Кінцевий індекс останнього входження: {index}")
print(f"Кількість порівнянь символів: {comparisons}")
