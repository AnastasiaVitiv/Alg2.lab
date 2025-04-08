class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

    def __lt__(self, other):
        return self.priority > other.priority

    def __repr__(self):
        return f"(Value: {self.value}, Priority: {self.priority})"


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, value, priority):
        node = Node(value, priority)
        self.heap.append(node)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_node = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return max_node

    def peek(self):
        return self.heap[0] if self.heap else None

    def is_empty(self):
        return len(self.heap) == 0

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def _heapify_down(self, index):
        size = len(self.heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index
            if left < size and self.heap[left] > self.heap[largest]:
                largest = left
            if right < size and self.heap[right] > self.heap[largest]:
                largest = right
            if largest == index:
                break
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            index = largest

    def __repr__(self):
        return str(self.heap)


if __name__ == "__main__":
    pq = PriorityQueue()
    pq.insert("A", 3)
    pq.insert("B", 5)
    pq.insert("C", 1)
    pq.insert("D", 4)

    print("Поточна черга:", pq)
    print("Максимальний елемент:", pq.extract_max())
    print("Поточна черга після вилучення:", pq)
