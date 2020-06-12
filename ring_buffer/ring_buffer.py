
from doubly_linked_list import DoublyLinkedList
# def __init__(self, limit=10):
#     self.limit = limit
#     self.size = 0
#     self.order = DoublyLinkedList()
#
#     self.storage = dict()


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_node = None
        self.storage = DoublyLinkedList()
# the capacity limit is set already in the test file no need to set it.
# bring in the doubly linked list from midweek project.

    def append(self, item):

        if self.storage.length < self.capacity:
            # run check to make sure length is below capacity

            self.storage.add_to_tail(item)
            # add to tail instead of head, the overall flow of the ring buffer and adding to tail and replacing the old data from the head.
            self.current_node = self.storage.head
            # sets current to the head
        else:
            # now storage is at capacity:
            if not self.current_node.next:
                # checking for a next
                # since/if there is no next then set the current node value to item and set the node to the head
                self.current_node.value = item
                self.current_node = self.storage.head
            else:
                # there IS a next for the node
                # set the node to the item

                self.current_node.value = item
                self.current_node = self.current_node.next
                # replaced the current / oldest node
        #

    def get(self):
        array = []
        # start with an empty array
        current = self.storage.head
        # declare current to head
        while current:
            array.append(current.value)
            # append array with the current value
            current = current.next
            # set the current to next
        return array
