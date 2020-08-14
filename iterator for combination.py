from itertools import combinations
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.characters=list(combinations(list(characters),combinationLength))
        self.combinationLength=combinationLength

    def next(self) -> str:
        ans=self.characters.pop(0)
        return ''.join(ans)

    def hasNext(self) -> bool:
        if self.characters:
            return True
        return False


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
