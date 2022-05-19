class father:
    def transporat(self):
        print("cycle")

class son(father):
    def transporat(self):
        print("bike")

obj = father()
obj.transporat()

obj = son()
obj.transporat()
