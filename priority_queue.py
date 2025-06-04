class PriorityQueue:
    def __init__(self):
        self.array = []
        
    def put(self, item):
        key = item[0]
        # else
        for i in range(len(self.array)):
            key_at_i = self.array[i][0]
            if key < key_at_i:
                self.array.insert(i, item)
                return
        # if this is the largest so far (or equal), it goes at the end
        self.array.append(item)
    def empty(self):
        return len(self.array) == 0
    def get(self):
        return self.array.pop(0)