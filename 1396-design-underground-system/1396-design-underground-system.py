class UndergroundSystem:

    def __init__(self):
        self.check_in = defaultdict(list)
        self.check_out = dict_of_dict = defaultdict(lambda: defaultdict(list))

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if self.check_in[id][0] not in  self.check_out[stationName]:
            self.check_out[stationName][self.check_in[id][0]] = [0, 0]
            
        self.check_out[stationName][self.check_in[id][0]][0] += t - self.check_in[id][1]
        self.check_out[stationName][self.check_in[id][0]][1] += 1
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.check_out[endStation][startStation][0] / self.check_out[endStation][startStation][1]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)