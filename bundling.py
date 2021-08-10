import sys

class TrieNode:
    def __init__(self, char):
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
                if len(node.children) == 1:
                   node.counter += 1
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        node.is_end = True
        



T = int(input())
t = Trie() 

for i in range(T):
    S, K = map(int,input().split()) #S = number of strings, K = number of Strings in Bundle
    G = int(S / K) # K devides S so G = number of bundles
    fixes = set()
    for j in range(S):
        words = list(map(str,input().split('\n')))
        for word in words:
            t.insert(word)
            fixes.add(t.counter)

    print(sum(fixes))




# t.insert("was")
# t.insert("word")
# t.insert("war")
# t.insert("what")
# t.insert("where")
# t.query("wh")
# print(t.query("wh"))