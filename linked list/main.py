class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
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

    def updateNode(self, val, index):
        current_node = self.head
        position = 0
        if position == int(index):
            current_node.data = val
        else:
            while (current_node != None and position != int(index)):
                position+= 1
                current_node = current_node.next

                if current_node != None:
                    current_node.data = val
                else:
                    print("Index not present")

    def removeFirstNode(self):
        if (self.head == None):
            return
        
        self.head = self.head.next

    def removeLastNode(self):
        if (self.head == None):
            return
        
        current_node = self.head
        while(current_node.next.next):
            current_node = current_node.next
        
        current_node.next = None

    def removeNodeAtIndex(self, index):
        if self.head == None:
            return
        
        current_node = self.head
        position = 0
        if (position == int(index)):
            self.removeFirstNode()
        else:
            while(current_node != None and position + 1 != index):
                position+= 1
                current_node = current_node.next

            if current_node != None:
                current_node.next = current_node.next.next
            else:
                print('Index not present')

    def removeNode(self, data):
        current_node = self.head
        if current_node.data == data:
            self.removeFirstNode()
            return
        
        while current_node != None and current_node.next.data == data:
            current_node = current_node.next

        if current_node != None:
            return
        else:
            current_node.next = current_node.next.next

    def printNode(self):
        current_node = self.head
        while current_node != None:
            print(current_node.data)
            current_node = current_node.next

    def nodeSize(self):
        size = 0
        if self.head:
            current_node = self.head
            while(current_node):
                size+= 1
                current_node = current_node.next
            return size
        else:
            return 0
        

# create a new linked list
llist = LinkedList()
 
# add nodes to the linked list
llist.insertAtend('a')
llist.insertAtend('b')
llist.insertAtBegin('c')
llist.insertAtend('d')
llist.insertAtIndex('g', 2)
 
# print the linked list
print("Node Data")
llist.printNode()
 
# remove a nodes from the linked list
print("\nRemove First Node")
llist.removeFirstNode()
print("Remove Last Node")
llist.removeLastNode()
print("Remove Node at Index 1")
llist.removeNodeAtIndex(1)
 
 
# print the linked list again
print("\nLinked list after removing a node:")
llist.printNode()
 
print("\nUpdate node Value")
llist.updateNode('z', 0)
llist.printNode()
 
print("\nSize of linked list :", end=" ")
print(llist.nodeSize())