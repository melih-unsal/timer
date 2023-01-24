from time import time

class Timer:
    def __init__(self,title="process"):
        self.title = title
        
    def __enter__(self):
        self.start = time()
        
    def __exit__(self, exc_type, exc_value, traceback):
        self.end = time()
        self.display()
        
    def display(self):
        diff = round(self.end - self.start,3)
        days = int(diff // 86400)
        hours = int(diff // 3600 % 24)
        minutes = int(diff // 60 % 60)
        seconds = int(diff % 60)
        ms = int(1000*diff % 1000)
        res = ""
        for amount,title in zip([days,hours,minutes,seconds,ms],["days","hours","minutes","seconds","ms"]):
            if amount > 1:
                res+=f"{amount} {title}, "
        res = res.strip().rstrip(",")
        if len(res) == 0:
            res = "-"
        print(self.title,":",res)
