def sort(arr):
    n = len(arr)
    for i in range(n - 1):
        max_idx = i
        for j in range(i + 1, n):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return arr

def find_largest_k(arr, k):
    if not arr:
        raise ValueError("Масив порожній")

    if k > len(arr) or k <= 0:
        raise ValueError("k має бути в межах від 1 до довжини масиву")

    sorted_arr = sort(arr[:])
    largest_k = sorted_arr[k - 1]
    index = [i for i, val in enumerate(arr) if val == largest_k]

    return largest_k, index


def main():
    try:
        input_array = input("Напиши масив: ")
        numbers_as_strings = input_array.split()
        arr = [int(num) for num in numbers_as_strings]
        k = int(input("Задай k: "))

        largest_k, index = find_largest_k(arr, k)
        print(f"Знайдений {k}-й найбільший елемент: {largest_k}")
        print(f"Позиція {k}-го найбільшого елемента в масиві: {index}")
    except ValueError as e:
        print(f"Помилка: {e}")


if __name__ == "__main__":
    main()
