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


if __name__ == '__main__':
    array = numpy.sort(numpy.random.uniform(-100000, 100000, size=100000000))

    num = array[random.randint(0, len(array) - 1)]

    start_time = timer()
    res = ternarySearch(array, num)
    end_time = timer() - start_time

    print(f"\n---------ternary search---------")
    print(f"\nsearching for {num}\nresult = {res}\nchecking(arr[{res}]) = {array[res]}")

    print(f"\n--- {end_time} seconds ---")
