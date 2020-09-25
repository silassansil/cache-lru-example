class Node():
    def __init__(self, key, data):
        self.next = None
        self.prev = None
        self.key = key
        self.data = data

    def __str__(self):
        return f'[{self.key}, {self.data}]'


class CacheLRU():
    def __init__(self, size):
        self.head = None
        self.tail = None
        self.table = {}
        self.size = size

    def put(self, key, data):
        value = self.table.get(key)

        if value is not None:
            value.data = data
            self.remove(value)
            self.addOfTop(value)

        else:
            node = Node(key, data)
            if len(self.table) >= self.size:
                self.table.pop(self.tail.key)
                self.remove(self.tail)

            self.addOfTop(node)
            self.table[key] = node

    def get(self, key):
        value = self.table.get(key)
        if value is not None:
            self.remove(value)
            self.addOfTop(value)
            return value

        return -1

    def addOfTop(self, node):
        node.next = self.head
        if self.head is not None:
            self.head.prev = node
        self.head = node

        if self.tail is None: self.tail = node

    def remove(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next is not None:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

    def print_list(self, node):
        if node is None: return
        print(self.table[node.key])
        self.print_list(node.next)


if __name__ == '__main__':
    dll = CacheLRU(5)
    dll.put(1, 2)
    dll.put(2, 3)
    dll.put(3, 6)
    dll.put(4, 5)
    dll.put(5, 2)
    dll.put(6, 3)
    dll.put(7, 7)

    dll.get(4)
    dll.print_list(dll.head)

    print('>>>>>>>>>>>>>>>>>>>>>')

    dll.get(7)
    dll.print_list(dll.head)





