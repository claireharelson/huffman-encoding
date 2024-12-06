# This script creates a class to define a heap object using an array implementation


class Heap:
    def __init__(self):
        """
        Holds items in a min heap data structure
        """
        self.heap = [('blank', 0)]
        self.size = 0
        self.left_child = None
        self.right_child = None
        self.parent = None
        self.root = None

    def parent(self, index):
        """
        Defines the parent of a node
        index: position of current node
        return: parent of current node
        """
        self.parent = self.heap[index // 2]
        return self.parent

    def left_child(self, index):
        """
        Defines the left child of a node
        index: position of current node
        return: left child
        """
        self.left_child = self.heap[(2 * index)]
        return self.left_child

    def right_child(self, index):
        """
        Defines the right child of a node
        index: position of current node
        return: right child
        """
        self.right_child = self.heap[(2 * index) + 1]
        return self.right_child

    def exchange(self, item1_index, item2_index):
        """
        Exchanges two nodes within a heap
        item1: first item to be swapped to item2's location
        item2: second item to be swapped to item1's location
        """
        self.heap[item1_index], self.heap[item2_index] = self.heap[item2_index], self.heap[item1_index]

    def insert(self, item) -> None:
        """
        Inserts an item into the min heap
        item: the item to insert
        """
        if type(item) is not int:
            try:
                # add the item to the heap, increase heap size, and check for proper min heap ordering
                if len(item) == 2:
                    item = (item[0], int(item[1]))
                else:
                    item = (item[0], int(item[1:]))
                self.heap.append(item)
                self.size += 1
                self.percolate_up(self.size)
            except AssertionError:
                print(f"This is an int type heap! Please don't input {type(item)}")

    def percolate_up(self, index):
        """
        Percolates an inserted item up to maintain min heap properties
        item: the item to be percolated up
        """
        ordered = False
        # if item is not the root node
        while (index // 2 > 0) and ordered is False:
            # exchange the items' positions if the new node is less than the parent node
            if self.heap[index][1] < self.heap[(index // 2)][1]:
                self.exchange(index, (index // 2))
            elif self.heap[index][1] == self.heap[(index // 2)][1]:
                if self.heap[index][0] < self.heap[(index // 2)][0]:
                    self.exchange(index, (index // 2))
            else:
                ordered = True
            # update the index
            index = index // 2

    def remove(self):
        """
        Removes one item from the heap and returns it
        return: the current item with the lowest priority (i.e. the root)
        """
        if self.size == 0:
            raise AssertionError("Heap is empty, cannot remove any other items.")
        else:
            to_remove = self.heap[1]
            self.heap[1] = self.heap[self.size]
            *self.heap, _ = self.heap
            self.size -= 1
            self.percolate_down(1)
            return to_remove

    def percolate_down(self, index):
        """
        Percolates an item down to maintain min heap properties
        item: the item to be percolated down
        """
        # if the current node has at least one child
        while index * 2 <= self.size:
            child = self.smaller_child(index)
            # swap the values of the current node if it is greater than its smaller child
            if self.heap[index][1] > self.heap[child][1]:
                self.exchange(index, child)
            elif self.heap[index][1] == self.heap[child][1]:
                if self.heap[index][0] > self.heap[child][0]:
                    self.exchange(index, child)
            index = child

    def smaller_child(self, index):
        """
        Designed to determine if a node's left or right child has a smaller value
        index: index of the current node
        return: index of a node's smaller child
        """
        # if the node only has one child, return this index
        if (index * 2) + 1 > self.size:
            return index * 2
        else:
            # if two children, return the index of the one with a smaller value
            if self.heap[index * 2][1] < self.heap[(index * 2) + 1][1]:
                return index * 2
            else:
                return (index * 2) + 1

    def traverse(self):
        """
        Allows for preorder traversal of a heap
        return: heap in preorder
        """
        preorder_heap = []
        for i in range(1, len(self.heap)):
            preorder_heap.append(str(self.heap[i]))
        if len(preorder_heap) == 0:
            print("The heap is currently empty.")
        else:
            return preorder_heap
