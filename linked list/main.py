class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
    

    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAtIndex(self,data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if position == int(index):
            self.insertAtBegin(data)
        else:
            while current_node != None and position+1 != int(index):
                position+= 1
                current_node = current_node.next

                if current_node != None:
                    new_node.next = current_node.next
                    current_node.next = new_node
                else:
                    print('Index not present')

    def insertAtend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        current_node = self.head
        while (current_node.next):
            current_node = current_node.next

        current_node.next = new_node