class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False


#  else: # the capacity has been reached
        # # check if the current node has a next
        # if not self.current_node.next:
        #     # if not, set the current node's value equal to the item
        #     # and set the current node to be the head
        #     self.current_node.value = item
        #     self.current_node = self.storage.head
        # else: # the current node has a next link
        #     # set the current node's value equal to the item
        #     # and move the current node to the next node to
        #     # replace that value as it is the next oldest
        #     self.current_node.value = item
        #     self.current_node = self.current_node.next
        #


    def reverse_list(self, node, prev):
        # need to reverse the order 1,2,3, none, into 3,2,1,none
        # singly linked list already established above
        # Does not need recursion, but can do it.
        # doing w/ a loop as per instructions
        # loop through and grab the previous
        prev = None
        current = self.head
        while current:
            # loop through and grab the previous entries the whole way through
            next = current.get_next()
            current.set_next(prev)
            prev = current
            current = next

        if prev:

            # if it is the previous then set the head to the previous
            self.head = prev
            # print!
            print(prev.value)
