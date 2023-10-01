class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def peek(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def size(self):
        return len(self.heap)

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smaller = index
        if (
            left_child_index < len(self.heap)
            and self.heap[left_child_index] < self.heap[smaller]
        ):
            smaller = left_child_index
        if (
            right_child_index < len(self.heap)
            and self.heap[right_child_index] < self.heap[smaller]
        ):
            smaller = right_child_index
        if smaller != index:
            self.heap[index], self.heap[smaller] = self.heap[smaller], self.heap[index]
            self._heapify_down(smaller)

heap = MinHeap()
heap.push(9)
heap.push(4)
heap.push(13)
heap.push(1)
heap.push(17)

print("Min Heap:")
while heap.size() > 0:
    print(heap.pop())
