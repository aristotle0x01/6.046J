

class MergeSort:
    # Constructor
    def __init__(self):
        return

    def merge_sort(self, array: [], low: int, high: int):
        if low < high:
            middle = (low + high)//2
            self.merge_sort(array, low, middle)
            self.merge_sort(array, middle+1, high)
            self.merge(array, low, middle, high)

        return

    def merge(self, array: [], low: int, middle: int, high: int):
        al = []
        ah = []
        for i in range(low, middle+1):
            al.append(array[i])
        for i in range(middle+1, high+1):
            ah.append(array[i])

        li = 0
        hi = 0
        ai = low
        while li < (middle-low+1) and hi < (high-(middle+1)+1):
            if al[li] <= ah[hi]:
                array[ai] = al[li]
                li = li + 1
            else:
                array[ai] = ah[hi]
                hi = hi + 1
            ai = ai + 1
        while li < (middle-low+1):
            array[ai] = al[li]
            li = li + 1
            ai = ai + 1
        while hi < (high-(middle+1)+1):
            array[ai] = ah[hi]
            hi = hi + 1
            ai = ai + 1

        return

    def merge_sort2(self, array: []):
        self.merge_sort(array, 0, len(array)-1)
        return array

ms = MergeSort()
print(ms.merge_sort2([56,88,110, 0,-1,2,1,4,3]))