class Items:
    def __init__(self):
        self.nodes = [{"type": 3, "size": 9},
                      {"type": 2, "size": 7},
                      {"type": 7, "size": 4},
                      {"type": 8, "size": 5},
                      ]
        self.weights=[1,2]

    def distances(self, item):
        result=[]
        for i in self.nodes:
            summ=0
            index=0
            print(i)
            for j in item.keys():
                print(i[j])
                summ+=(i[j]-item[j])**2*self.weights[index]
                index+=1
            result.append(summ)
        return sorted(result)

print(Items().distances({"type": 2, "size": 7}))