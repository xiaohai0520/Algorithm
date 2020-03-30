class UndergroundSystem:

    def __init__(self):
        self.dic = collections.defaultdict(dict)
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.dic[stationName][id] = t
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.dic[stationName][id] = t

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total = 0
        count = 0
        for id in self.dic[endStation]:
            if id in self.dic[startStation]:
                count += 1
                total += (self.dic[endStation][id] - self.dic[startStation][id])
        return total/count
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
