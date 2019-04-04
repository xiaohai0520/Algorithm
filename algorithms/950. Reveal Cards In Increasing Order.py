class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        if len(deck) < 2:
            return deck
        if len(deck) < 3:
            return sorted(deck)
        
        deck.sort()
        res = [deck.pop()]
        while deck:
            res.insert(0,res.pop())
            res.insert(0,deck.pop())
            
        return res
        
