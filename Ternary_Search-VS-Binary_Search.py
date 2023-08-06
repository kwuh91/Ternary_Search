import numpy
from numpy import random
from timeit import default_timer as timer


def ternarySearch(arr: [float], key: float, left: int = 0, right: int = None) -> int:
    if right is None: right = len(arr) - 1
    if left <= right:

        mid1: int = left + (right - left) // 3
        mid2: int = right - (right - left) // 3

        if arr[mid1] == key: return mid1
        if arr[mid2] == key: return mid2

        if key < arr[mid1]:
            return ternarySearch(arr, key, left, mid1 - 1)
        elif key > arr[mid2]:
            return ternarySearch(arr, key, mid2 + 1, right)
        else:
            return ternarySearch(arr, key, mid1 + 1, mid2 - 1)

    return -1


def bin_search(arr: [float], num: float) -> int:
    low = 0
    high = len(arr) - 1
    while low <= high:
        guess = arr[(low + high) // 2]
        if guess == num:
            return (low + high) // 2
        elif guess < num:
            low = (low + high) // 2 + 1
        else:
            high = (low + high) // 2 - 1
    return None

if __name__ == '__main__':
    array = numpy.sort(numpy.random.uniform(-100000, 100000, size=1000000000))

    num = array[random.randint(0, len(array) - 1)]

    start_time = timer()
    res = ternarySearch(array, num)
    end_time = timer() - start_time

    start_time2 = timer()
    res2 = bin_search(array, num)
    end_time2 = timer() - start_time

    print(f"TEST FOR {1000000000} ELEMENTS")
    print(f"\n---------ternary search---------")
    print(f"\nsearching for {num}\nresult = {res}\nchecking(arr[{res}]) = {array[res]}")

    print(f"\n--- {end_time} seconds ---")

    print(f"\n\n---------binary search---------")
    print(f"\nsearching for {num}\nresult = {res2}\nchecking(arr[{res2}]) = {array[res2]}")

    print(f"\n--- {end_time2} seconds ---")
