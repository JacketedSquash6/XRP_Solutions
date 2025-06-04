class PriorityQueue:
    def __init__(self):
        self.array = []
        
    def put(self, item):
        (key, _value) = item
        # else
        for i in range(len(self.array)):
            (key_at_i, _val_at_i) = self.array[i]
            if key < key_at_i:
                self.array.insert(i, item)
                return
        # if this is the largest so far (or equal), it goes at the end
        self.array.append(item)
    def empty(self):
        return len(self.array) == 0
    def get(self):
        return self.array.pop(0)