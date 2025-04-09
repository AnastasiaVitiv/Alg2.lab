import unittest
from lab5 import find_min_depth

def run_test(test_name, root, graph, expected):
    result = find_min_depth(root, graph)
    if result == expected:
        print(f"{test_name} пройдено")
    else:
        print(f"{test_name} НЕ пройдено. Очікувалось: {expected}, Отримано: {result}")

def test_all():
    run_test(
        "Тест 1: Одне кореневе дерево",
        1,
        {},
        1
    )

    run_test(
        "Тест 2: Просте дерево",
        1,
        {
            1: [2, 3],
            2: [4],
            3: [6]
        },
        3
    )

    run_test(
        "Тест 3: Тільки ліва гілка",
        1,
        {
            1: [2],
            2: [3],
            3: []
        },
        3
    )

    run_test(
        "Тест 4: Листок на другому рівні",
        1,
        {
            1: [2, 3],
            2: [],
            3: [4]
        },
        2
    )

    run_test(
        "Тест 5: Порожнє дерево",
        1,
        {
        },
        1
    )

if __name__ == "__main__":
    test_all()
