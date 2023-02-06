class DetectSquares:

    def __init__(self):
        self.d = collections.defaultdict(collections.Counter)    # (x, y) : count

    def add(self, point: List[int]) -> None:
        x, y = point
        self.d[x][y] += 1

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        res = 0
        for y2 in self.d[x1]:
            if y2 == y1:
                continue
            
            side = abs(y2 - y1)
            # left
            res += self.d[x1-side][y1] * self.d[x1-side][y2] * self.d[x1][y2]
            
            # right
            res += self.d[x1+side][y1] * self.d[x1+side][y2] * self.d[x1][y2]
            
        return res