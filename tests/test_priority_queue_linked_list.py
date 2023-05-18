import pytest
from ..PriorityQueueLinkedList import PriorityQueueLinkedList

@pytest.fixture
def priority_queue() -> PriorityQueueLinkedList:
    return PriorityQueueLinkedList()


class TestPriorityQueueLinkedList:
    def test_is_empty(self, priority_queue: PriorityQueueLinkedList) -> None:
        assert priority_queue.is_empty() == True
        priority_queue.insert(0)
        assert priority_queue.is_empty() == False

    def test_insert(self, priority_queue: PriorityQueueLinkedList) -> None:
        assert str(priority_queue) == 'Empty queue'
        priority_queue.insert(0)
        priority_queue.insert(5)
        priority_queue.insert(10)
        assert str(priority_queue) == ' 0 5 10'

    def test_pop(self, priority_queue: PriorityQueueLinkedList) -> None:
        priority_queue.insert(0)
        priority_queue.insert(5)
        priority_queue.insert(10)
        priority_queue.insert(1)
        assert str(priority_queue) == ' 0 1 5 10'
        priority_queue.pop()
        assert str(priority_queue) == ' 1 5 10'
        priority_queue.pop()
        assert str(priority_queue) == ' 5 10'
        priority_queue.pop()
        assert str(priority_queue) == ' 10'
        priority_queue.pop()
        assert str(priority_queue) == 'Empty queue'
