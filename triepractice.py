class TrieNode():
    def __init__(self, c):
        self.c = c
        self.is_end = False
        self.children = {}
        self.node_count

class Trie(object):
    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word):
        node = self.root

        for c in word:
            if c in node.children:
                node = node.children[c]
                node.node_count += 1
            else:
                new_node = TrieNode(c)
                node.children[c] = new_node
                node = new_node
        node.is_end = True

    def dfs(self, node, pre):

        if node.is_end:
            self.output.append((pre + node.c))

        for child in node.children.values():
            self.dfs(child, pre + node.c)
            
    def search(self, searchstring):
        node = self.root

        for char in searchstring:
            if char in node.children.values():
                node = node.children[char]
            else: 
                return []
        self.output = []
        self.dfs(node, searchstring[:-1])
        print(self.output)

n, q = [int(x) for x in input().split()]
t = Trie()
for i in range(n):
    
    a, b = input().split()
    t.insert(a, b)
    
for i in range(q):
    t.search(input())

# t = Trie()
# t.insert("word")
# t.insert("was")
# t.insert("war")
# t.insert("what")
# t.insert("what")
# t.insert("where")

# t.search("wh")

