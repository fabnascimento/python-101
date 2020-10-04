# Node class implementation
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_data(self, val):
        self.val = val

    def get_data(self):
        return self.val

    def get_next(self):
        return self.next
    
    def set_next(self, next):
        self.next = next

#LinkedList class definition
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.count = 0

    def get_count(self):
        return self.count

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1

    def find(self, val):
        item = self.head
        while(item != None):
            if (item.get_data() == val):
                return item
            else:
                item = item.get_next()
        
        return None

    def delete_at(self, index):
        if (index > self.count-1):
            return
        if (index == 0):
            self.head = self.head.get_next()
        else:
            temp_index = 0
            node = self.head
            while temp_index < index-1:
                node = node.get_next()
                temp_index += 1
            node.set_next(node.get_next().get_next())
        self.count -= 1

    def dump_list(self):
        temp_node = self.head
        while temp_node != None:
            print("Node: ", temp_node.get_data())
            temp_node = temp_node.get_next()



itemList = LinkedList()
itemList.insert(38)
itemList.insert(25)
itemList.insert(26)
itemList.insert(1337)
itemList.dump_list()

print("Item count: ", itemList.get_count())
print("Finding item: ", itemList.find(26))

# testing delete at 
print("Item count before removal: ", itemList.get_count())
itemList.delete_at(itemList.count-1)
itemList.dump_list()
print("Item count after deletion: ", itemList.get_count())

