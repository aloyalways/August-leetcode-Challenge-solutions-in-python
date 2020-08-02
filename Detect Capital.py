class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word)==1:
            return True
        first=word[0].isupper()
        if first:
            second=word[1].isupper()
            if second:
                for i in range(2,len(word)):
                    if word[i].islower():
                        return False
                else:
                    return True
            else:
                for i in range(2,len(word)):
                    if word[i].isupper():
                        return False
                else:
                    return True
        else:
            for i in word:
                if i.isupper():
                    return False
            else:
                return True
            
