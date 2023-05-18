import random, timeit
from PriorityQueueArray import PriorityQueueArray
from PriorityQueueLinkedList import PriorityQueueLinkedList

DATA_NUMBERS_COUNT = 10000

random.seed(42)

priority_queue_array = PriorityQueueArray()
priority_queue_linked_list = PriorityQueueLinkedList()

# Generate random data numbers
data = [random.randint(1, 1000) for _ in range(DATA_NUMBERS_COUNT)]

# Calculate times tests
def time_test_insert_priority_queue_array() -> None:
    for item in data:
        priority_queue_array.insert(item)


def time_test_insert_priority_queue_linked_list() -> None:
    for item in data:
        priority_queue_linked_list.insert(item)


def time_test_pop_priority_queue_array() -> None:
    for _ in range(DATA_NUMBERS_COUNT):
        priority_queue_array.pop()


def time_test_pop_priority_queue_linked_list() -> None:
    for _ in range(DATA_NUMBERS_COUNT):
        priority_queue_linked_list.pop()


time_insert_priority_queue_array = timeit.timeit(time_test_insert_priority_queue_array, number=1)
time_insert_priority_queue_linked_list = timeit.timeit(time_test_insert_priority_queue_linked_list, number=1)
time_pop_priority_queue_array = timeit.timeit(time_test_pop_priority_queue_array, number=1)
time_pop_priority_queue_linked_list = timeit.timeit(time_test_pop_priority_queue_linked_list, number=1)

# Results
print(f'Time for insert in priority queue array: {time_insert_priority_queue_array}')
print(f'Time for insert priority queue linked list: {time_insert_priority_queue_linked_list}')
print(f'Time for pop in priority queue array: {time_pop_priority_queue_array}')
print(f'Time for pop priority queue linked list: {time_pop_priority_queue_linked_list}')
