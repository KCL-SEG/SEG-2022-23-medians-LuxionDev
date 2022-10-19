"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1
 
 
def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

    return array


def median(array):
    if len(array) % 2 == 0:
        high = array[int(len(array) / 2)]
        low = array[int((len(array) / 2) - 1)]
        val = (high + low) / 2
    else:
        val = array[int((len(array) - 1)/ 2)]

    return val


while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        numbers = quickSort(numbers, 0, len(numbers) - 1)
        numbers = median(numbers)
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)