class Solution:
    def reformatDate(self, date: str) -> str:
        d = date.split()
        month = ["dummy", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        
        mm = "0" + str(month.index(d[1])) if month.index(d[1]) < 10 else str(month.index(d[1]))
        dd = "0" + d[0][0] if len(d[0]) == 3 else d[0][:2]
        yy = d[-1]
        return yy + "-" + mm + "-" + dd 