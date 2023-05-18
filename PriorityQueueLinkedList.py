from typing import Optional

class QueueItem:
    def __init__(self, item: Optional[int]) -> None:
        self.item: Optional[int] = item
        self.next: Optional[QueueItem] = None
        self.prev: Optional[QueueItem] = None


class PriorityQueueLinkedList:
    def __init__(self) -> None:
        self.head = QueueItem(None)
        self.head.next = self.head.prev = self.head

    def __str__(self) -> str:
        to_print = ''
        if self.is_empty():
            return 'Empty queue'
        else:
            current = self.head.next
            while current != self.head:
                if current is not None:
                    to_print += ' ' + str(current.item)
                    current = current.next

        return to_print

    def is_empty(self) -> bool:
        """ Return True if the queue is empty """

        return self.head.next == self.head

    def insert(self, item: int) -> None:
        """ Insert item into queue """

        new_queue_item = QueueItem(item)
        current = self.head.next
        while current != self.head and (current is not None and current.item is not None and current.item <= item):
            current = current.next

        if current is not None and current.prev is not None:
            new_queue_item.prev = current.prev
            new_queue_item.next = current
            current.prev.next = new_queue_item
            current.prev = new_queue_item

    def pop(self) -> Optional[int]:
        """ Remove item from queue """

        if self.is_empty():
            return None

        if self.head.next is not None:
            item = self.head.next.item
            self.head.next = self.head.next.next

            if self.head is not None and self.head.next is not None:
                self.head.next.prev = self.head

            return item

        return None
