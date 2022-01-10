

class QuickSort:
    # Constructor
    def __init__(self):
        return

    def quick_sort(self, array: [], low: int, high: int):
        if low < high:
            middle = self.partition(array, low, high)
            self.quick_sort(array, low, middle-1)
            self.quick_sort(array, middle+1, high)

        return

    # pick the last element as pivot
    def partition(self, array: [], low: int, high: int):
        index = low
        for i in range(low, high):
            if array[i] < array[high]:
                array[index], array[i] = array[i], array[index]
                index = index + 1
        array[index], array[high] = array[high], array[index]
        return index

    # pick the last element as pivot
    def partition2(self, array: [], low: int, high: int):
        left = []
        right = []

        for i in range(low, high):
            if array[i] > array[high]:
                right.append(array[i])
            else:
                left.append(array[i])

        if len(right) != 0:
            left.append(array[high])
        else:
            right.append(array[high])

        index = low
        for t in left:
            array[index] = t
            pivot = index
            index = index + 1
        for r in right:
            array[index] = r
            index = index + 1
        return pivot

    def sort(self, array: []):
        self.quick_sort(array, 0, len(array)-1)
        return array


s = QuickSort()
print(s.sort([0,0,1000,29,2,1,4,3,56]))