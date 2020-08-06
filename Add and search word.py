class WordDictionary:

    def __init__(self):
        self.root={}
        

    def addWord(self, word: str) -> None:
        curr_node=self.root
        if not self.search(word):
            for letter in word:
                if letter not in curr_node:
                    curr_node[letter]={}
                curr_node=curr_node[letter]
            curr_node["*"]={}
        

    def search(self, word: str) -> bool:
        curr_node=self.root
        def helper(start,curr_node):
            if start>=len(word):
                if "*" in curr_node:
                    return True
                else:
                    return False
            
            if word[start]==".":
                for k,v in curr_node.items():
                    if helper(start+1,v):
                        return True
                return False
            elif word[start] in curr_node:
                if helper(start+1,curr_node[word[start]]):
                    return True
            else:
                return False
        return helper(0,curr_node)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
