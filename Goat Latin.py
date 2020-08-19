class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowel=['a','e','i','o','u']
        S=list(map(str,S.split(' ')))
        ans=""
        As=1
        for i in S:
            if i[0].lower() in vowel:
                ans+=i+"ma"+"a"*As+" "
            else:
                ans+=i[1:]+i[0]+"ma"+"a"*As+" "
            As+=1
        return ans[:len(ans)-1]
                
