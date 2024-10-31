# Methods to append at head or at last


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLL:
    def __init__(self):
        self.head = None  # Assigning head to first node

    # To add a Node
    def append(self, val):
        newnode = Node(val)  # Assigning the node value to var
        if self.head == None:
            self.head = newnode
        else:
            curr = self.head  # If first node is not empty, curr var to iterate

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

    # To insert a node at beiginning(head) even if existiong head exits
    def insertHead(self, val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head  # newnode at first
            self.head = new_node  # updating head
        print()

    def insertposi(self, val, posi):
        new_node = Node(val)
        if posi == 0:
            new_node.next = (
                self.head
            )  # assigning address of next node(ie now 2nd) to new node(ie now 1st)
            self.head = new_node  # updating head pointer to point
        else:
            curr = self.head
            prev = None  # 2 pointers to track of prev and current node and update their address after inserting new node
            count = 0
            while curr != None and count < posi:
                prev = curr
                curr = curr.next
                count += 1
            new_node.next = curr  # takes address of adjacent node to its right
            prev.next = new_node  # takes address of adjacent node to its left

    # deleitng first Node
    def deleteNode(self):
        if self.head == None:
            print("Nothing to delete")
        else:
            temp = self.head  # now 1st node is known as temp
            self.head = self.head.next  # New head node

    # deleting by value

    def delbyVal(self, val):
        temp = self.head

        # Check if the list is empty
        if temp == None:
            print("List is empty")
            return

        # Check if the head node contains the value to delete
        if temp.val == val:
            self.head = temp.next
            return

        # Traverse the list to find the node to delete
        prev = None
        while temp != None:
            if temp.val == val:
                prev.next = temp.next  # Bypass the node to delete it
                return
            prev = temp
            temp = temp.next

        # If the node was not found

        print("Node not Found")


sll = SinglyLL()
sll.traverse()
sll.append(10)
sll.append(20)
sll.append(30)
sll.traverse()
sll.insertposi(100, 2)
sll.traverse()
sll.insertHead(4)
sll.traverse()
sll.delbyVal(20)
sll.traverse()
