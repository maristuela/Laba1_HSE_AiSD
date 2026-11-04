import random
from functional import (two_ukas, bin_serch_two_arr, exp_serch_two_arr,
                        double_bin_search_two_arr)

def test_all():
    cases = [
        ([1, 2, 3], [3, 4, 5], True), ([2, 4, 6], [3, 5, 7], False),
        ([], [], False), ([], [1, 2], False), ([1, 2], [], False),
        ([5], [5], True), ([5], [6], False),
        ([-5, -1], [-3, -1], True), ([-5, -3], [-4, -2], False),
        ([2, 4, 8, 10], [3, 5, 8, 12], True),
        ([10, 20, 25, 30], [15, 25, 35, 45], True),
    ]
    algorithms = [two_ukas, bin_serch_two_arr, exp_serch_two_arr, double_bin_search_two_arr]
    for a, b, expected in cases:
        for func in algorithms:
            assert func(a, b) == expected, f"Ошибка в {func.__name__} на {a}, {b}"
    print("Фиксированные тесты пройдены")

def test_random():
    random.seed(42)
    algorithms = [two_ukas, bin_serch_two_arr, exp_serch_two_arr, double_bin_search_two_arr]
    for i in range(1000):
        m, n = random.randint(0, 50), random.randint(0, 50)
        a = sorted(random.randint(-100, 100) for _ in range(m))
        b = sorted(random.randint(-100, 100) for _ in range(n))
        expected = bool(set(a) & set(b))
        for func in algorithms:
            assert func(a, b) == expected, f"Ошибка в {func.__name__} на {a}, {b}"
    print("1000 тестов пройдено")

if __name__ == '__main__':
    test_all()
    test_random()