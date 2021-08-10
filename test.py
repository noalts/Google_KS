class TrieNode:
    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.children = {}

# initialising empty TrieNode
class Trie(object):
    def __init__(self):
        self.root = TrieNode("")

# perform insertion into Trie

    def insert(self, word):
        node = self.root
        lenword = len(word)

        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        node.is_end = True

    def dfs(self, node, pre):
    
        if node.is_end:
            self.output.append((pre + node.char))
            
        for child in node.children.values():
            self.dfs(child, pre + node.char)

    def search(self, x):
            node = self.root
            
            for char in x:
                if char in node.children:
                    node = node.children[char]
                else:              
                    return []         
            self.output = [] 
            self.dfs(node, x[:-1])
            return self.output

T = int(input())
Strings = []
for i in range(T):
    Nlines, Kwords_in_group = [int(k) for k in input().split()]
    gr_amount = Nlines / Kwords_in_group
    
    for j in range(Nlines):
        Strings.append(input())
    
    for word in Strings:
        tr = Trie()
        tr.insert(word)
    
    
    Strings = []
