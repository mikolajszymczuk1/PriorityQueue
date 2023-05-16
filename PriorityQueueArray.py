from typing import Optional

class PriorityQueueArray:
    def __init__(self) -> None:
        self.queue: list[int] = []

    def __str__(self) -> str:
        return ' '.join([str(item) for item in self.queue])

    def is_empty(self) -> bool:
        """ Return True if the queue is empty """

        return len(self.queue) == 0

    def insert(self, item: int) -> None:
        """ Add new item to the queue """

        self.queue.append(item)

    def pop(self) -> Optional[int]:
        """ Remove item from the queue """

        if self.is_empty():
            return None

        index = 0
        for i in range(1, len(self.queue)):
            if self.queue[i] < self.queue[index]:
                index = i

        return self.queue.pop(index)
