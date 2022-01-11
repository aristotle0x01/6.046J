

class HeapSort:
    # Constructor
    def __init__(self):
        inner_heap = []
        n = 0
        capacity = 0
        return

    def pq_init(self, array: []):
        self.inner_heap = [0] * (len(array) + 1)
        self.n = 0
        self.capacity = len(array)
        return

    def heap_sort(self, array: []):
        self.pq_init(array)
        self.make_heap(array)
        for i in range(len(array)):
            x = self.extract_min()
            array[i] = x

        return

    def pq_parent(self, i: int):
        if i == 1:
            return -1
        else:
            return i // 2

    def pq_young_child(self, i: int):
        return 2 * i

    def pq_insert(self, x: int):
        self.n = self.n + 1
        self.inner_heap[self.n] = x
        self.bubble_up(self.n)
        return

    def bubble_up(self, i: int):
        p = self.pq_parent(i)
        if p == -1:
            return

        if self.inner_heap[i] < self.inner_heap[p]:
            self.inner_heap[p], self.inner_heap[i] = self.inner_heap[i], self.inner_heap[p]
            return self.bubble_up(p)

    def make_heap(self, array: []):
        for t in array:
            self.pq_insert(t)
        return

    def extract_min(self):
        if self.n == 0:
            return None

        min = self.inner_heap[1]
        self.inner_heap[1] = self.inner_heap[self.n]
        self.n = self.n - 1
        if self.n > 1:
            self.bubble_down(1)

        return min

    def bubble_down(self, i: int):
        c = self.pq_young_child(i)
        down = i
        for j in range(0, 2):
            if (c+j) <= self.n and self.inner_heap[c+j] < self.inner_heap[down]:
                down = c + j

        if down != i:
            self.inner_heap[down], self.inner_heap[i] = self.inner_heap[i], self.inner_heap[down]
            self.bubble_down(down)
        return

    def sort(self, array: []):
        self.heap_sort(array)
        return array


s = HeapSort()
print(s.sort([100,-1,56,2,1,4,3]))