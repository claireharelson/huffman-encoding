# This file will do the actual work of encoding and decoding through a huffman tree

code = dict()


class NodeTree:
    """
    Class to define a tree node and its children
    left: left child of node
    right = right child of node
    """
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return self.left, self.right


def huffman_tree(node, binary='') -> dict:
    """
    Function to implement the huffman coding algorithm
    return: dictionary values mapping a letter to its binary string code
    """
    if type(node) is str:
        return {node: binary}
    (left, right) = node.children()
    code.update(huffman_tree(left, binary + '0'))
    code.update(huffman_tree(right, binary + '1'))
    return code


def merge_items(nodes):
    """
    Function to merge the nodes of the frequency table heap
    nodes: nodes of heap
    return: root node of the newly merged heap
    """
    while len(nodes) > 1:
        (key1, freq1) = nodes[-1]
        (key2, freq2) = nodes[-2]
        nodes = nodes[:-2]
        node = NodeTree(key1, key2)
        nodes.append((node, freq1 + freq2))
    return nodes[0][0]


def encode(word):
    """
    Function to encode a clear text string using the code dictionary created by the huffman tree
    word: clear text string to encode
    return: encoded string in binary
    """
    word = str(word)
    for letter in word:
        for (key, value) in code.items():
            if letter == key:
                word = word.replace(letter, value)
    return word


def decode(numbers):
    """
    Function to decode an encoded string in binary using the code dictionary created by the huffman tree
    word: encoded string in binary to decode
    return: decoded string in clear text
    """
    number = str(numbers)
    for item in number:
        for (key, value) in code.items():
            if item == value:
                number = number.replace(item, key)
    return number
