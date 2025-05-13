import heapq

class HuffmanTreeNode:

    def __init__(self, freq, char = None, left = None, right = None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right

class HuffmanEncoder:

    def __init__(self, frequencies: dict):
        self.frequencies = frequencies
        self.encoding_map = {}
        self.encoding_map_reverse = {}
        self.tree_root = None

        self.build_tree()
        self.build_encoding_map()

    def build_tree(self):

        heap = [(freq, HuffmanTreeNode(char = char, freq = freq)) for char, freq in self.frequencies.items()]
        heapq.heapify(heap)

        while len(heap) > 1:
            # pop two least frequent
            (left_freq, left_node) = heapq.heappop(heap)
            (right_freq, right_node) = heapq.heappop(heap)
            
            # Combine frequency
            # Create new node with lower freq as left child and higher freq as right child
            new_freq = (left_freq + right_freq)
            new_node = HuffmanTreeNode(freq = new_freq, left = left_node, right = right_node)

            # re-insert to queue
            heapq.heappush(heap, (new_freq, new_node))

        # The last node is the root of the tree
        (_, self.tree_root) = heapq.heappop(heap)
        
    def build_encoding_map(self):

        q = [(self.tree_root, "")]

        # From root, build string while traversing to leaf nodes (leaf nodes have char and no children)
        while q:
            (curr_node, path) = q.pop()

            # If char node, set encoding for char as path string
            if curr_node.char is not None:
                self.encoding_map[curr_node.char] = path
                self.encoding_map_reverse[path] = curr_node.char

            # If go left, build path string with 0
            if curr_node.left:
                q.append((curr_node.left, path + "0"))

            # If go right, build path string with 1
            if curr_node.right:
                q.append((curr_node.right, path + "1"))

    def print_state(self):
        print(self.encoding_map)

    def encode(self, text: str) -> str:

        result = []

        for char in text:
            result.append(self.encoding_map[char])

        return "".join(result)

    def decode(self, encoded_text: str) -> str:

        curr = ""
        result = []

        for char in encoded_text:
            curr += char
            if curr in self.encoding_map_reverse:
                result.append(self.encoding_map_reverse[curr])
                curr = ""
        
        return "".join(result)

if __name__ == "__main__":

    freq_map = {"A": 9, "B": 2, "C": 4, "D": 5, "E": 8, "F": 1}

    huffman = HuffmanEncoder(freq_map)
    huffman.print_state()

    encode1 = huffman.encode("ABC")
    print(encode1)

    decode1 = huffman.decode(encode1)
    print(decode1)
    