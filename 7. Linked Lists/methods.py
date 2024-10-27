# Methods to append at head or at last


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLL:
    def __init__(self):
        self.head = None  # Assigning head to first node

    def append(self, val):
        newnode = Node(val)
        if self.head == None:
            self.head = Node(val)
        else:
            curr = self.head

            while curr.next != None:
                curr = curr.next  # to keep traversing current

            curr.next = newnode

    # To traverse and print all nodes value

    def traverse(self):
        if self.head == None:
            print("SLL is empty")
        else:
            curr = self.head
            while (
                curr != None
            ):  # This allows to traverse till last even till last node and print its value
                print(curr.val, end=" ")
                curr = curr.next
            print()


sll = SinglyLL()
sll.traverse()
sll.append(10)
sll.append(20)
sll.append(30)
sll.traverse()
