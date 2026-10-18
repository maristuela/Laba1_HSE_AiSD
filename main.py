import csv
import time

from functional import two_ukas, bin_serch, bin_serch_two_arr, exp_serch_two_arr, double_bin_search_two_arr


def create_case(m, n):
    arr2 = [2 * i + 1 for i in range(n)]

    if m > 0:
        step = (2 * n) / m
        arr1 = [int(2 * (i * step // 2)) for i in range(m)]
    else:
        arr1 = []

    return arr1, arr2

def create_degenerate_case(m, n):
    arr2 = [2 * i + 1 for i in range(n)]
    arr1 = [2 * n + 1 + 2 * i for i in range(m)]
    return arr1, arr2

def test_time(arr1, arr2):
    res = []
    print(f"_________________________________")
    k = 5
    s = 0
    for _ in range(k):
        t0 = time.perf_counter()
        two_ukas(arr1, arr2)
        t1 = time.perf_counter()
        s += t1 - t0
    result = s / k
    print(result)
    res.append(result)

    s = 0
    for _ in range(k):
        t0 = time.perf_counter()
        bin_serch_two_arr(arr1, arr2)
        t1 = time.perf_counter()
        s += t1 - t0
    result = s / k
    print(result)
    res.append(result)

    s = 0
    for _ in range(k):
        t0 = time.perf_counter()
        r = exp_serch_two_arr(arr1, arr2)
        t1 = time.perf_counter()
        s += t1 - t0
    result = s / k
    print(result)
    res.append(result)

    s = 0
    for _ in range(k):
        t0 = time.perf_counter()
        double_bin_search_two_arr(arr1, arr2)
        t1 = time.perf_counter()
        s += t1 - t0
    result = s / k
    print(result)
    res.append(result)

    return res

def write_csv(rows, filename="results.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["M", "N", "algorithm", "time_sec", "type"])
        writer.writerows(rows)
    print(f"Сохранено!")

def main():
    algorithms_names = [
        "two_ukas",
        "bin_serch_two_arr",
        "exp_serch_two_arr",
        "double_bin_search_two_arr",
    ]

    cases = [
        (10 ** 2, 10 ** 2, "normal"),
        (10 ** 3, 10 ** 3, "normal"),
        (10 ** 4, 10 ** 4, "normal"),
        (10**5, 10**5, "normal"),
        (10**6, 10**6, "normal"),
        (10**7, 10**7, "normal"),

        (10 ** 2, 10 ** 8, "normal"),
        (10**3, 10**8, "normal"),
        (10 ** 4, 10 ** 8, "normal"),
        (10**5, 10**8, "normal"),
        (10**6, 10**8, "normal"),
        (10**7, 10**8, "normal"),

        (10 ** 8, 10 ** 2, "normal"),
        (10 ** 8, 10 ** 3, "normal"),
        (10 ** 8, 10 ** 4, "normal"),
        (10**8, 10**5, "normal"),
        (10**8, 10**6, "normal"),
        # (10**8, 10**7, "normal"),

        (10 ** 2, 10 ** 8, "degenerate"),
        (10 ** 3, 10 ** 8, "degenerate"),
        (10 ** 4, 10 ** 8, "degenerate"),
        (10**5, 10**8, "degenerate"),
        (10**6, 10**8, "degenerate"),
        (10 ** 7, 10 ** 8, "degenerate"),
    ]

    rows = []
    for m, n, case_type in cases:
        print(f"\n[{case_type}] M = {m}, N = {n}")

        if case_type == "degenerate":
            arr1, arr2 = create_degenerate_case(m, n)
        else:
            arr1, arr2 = create_case(m, n)

        res = test_time(arr1, arr2)
        for l in range(4):
            rows.append([m, n, algorithms_names[l], res[l], case_type])
        del arr1, arr2

    write_csv(rows, "results.csv")

if __name__ == '__main__':
    main()
