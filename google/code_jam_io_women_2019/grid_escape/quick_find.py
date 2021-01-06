class QuickFind:
    def __init__(self, size):
        self.id = [i for i in range(0, size)]
        
    def union(self, p, q):
        pid = self.id[p]
        qid = self.id[q]
        
        for i in range(0, len(self.id)):
            if self.id[i] == qid:
                self.id[i] = pid
    
    def connected(self, p, q):
        return self.id[p] == self.id[q]