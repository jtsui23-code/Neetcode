class TimeMap:

    def __init__(self):
        self.ds = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key in self.ds:
            self.ds[key].append((value, timestamp))
        else:
            self.ds[key] = []
            self.ds[key].append((value, timestamp))


    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.ds:
            return ""
        
        array = self.ds[key]

        l = 0
        r = len(array) - 1

        large = -1

        while l <= r:
            
            m = (l+r)//2

            if array[m][1] <= timestamp:
                if large == -1:
                    large = m
                
                elif array[m][1] > array[large][1]:
                    large = m

                l = m + 1

            else:
                r = m - 1


        
        if large == -1:
            return ""
        
        return array[large][0]
        







        
