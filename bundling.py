import sys

class TrieNode:
    def __init__(self,char):
        self.char = char
        self.is_end = False
        self.counter = 0
        self.children = {}

class Trie(object):
    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word):
        node = self.root        
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        node.is_end = True
        node.counter += 1
    
    def dfs(self, node, prefix):
        if node.is_end:
            self.output.append((prefix + node.char, node.counter))
        
        for child in node.children.values():
            self.dfs(child, prefix + node.char)

    def query(self, x):
        self.output = []
        node = self.root

        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                return []
        
        self.dfs(node, x[:-1])

        return sorted(self.output, key=lambda x: x[1], reverse=True)
    
    # def list_words(self, Trie):
    #     fixes = []
    #     for k,v in Trie.items():
    #         for el in list_words(v):
    #             fixes.append(k+el)
    #     return fixes

T = int(input())
t = Trie() 

for i in range(T):
    S, K = map(int,input().split()) #S = number of strings, K = number of Strings in Bundle
    G = int(S / K) # K devides S so G = number of bundles
    fixes = []
    for j in range(S):
        words = list(map(str,input().split('\n')))
        for word in words:
            t.insert(word)
        for word in words:
            for char in word:
                if char.is_end is False:
                    t.query(char)
    print(t.query(char))    
    fixes = sorted(fixes)
    print(fixes)    




# t.insert("was")
# t.insert("word")
# t.insert("war")
# t.insert("what")
# t.insert("where")
# t.query("wh")
# print(t.query("wh"))