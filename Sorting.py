# Bubble Sort
def bubbleSort(array):
    sorted = False

    while not sorted:
        sorted = True
        for i in range(len(array)- 1):
            if array[i] > array[i+1]:
                sorted = False
                array[i], array[i+1] = array[i+1], array[i]
    return array

#print(bubbleSort([3,5,1,9,4,5,5, 45, 847, 536]))

#insertion sort
def insertionSort(array):