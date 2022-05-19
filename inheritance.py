class parent:
    def display(self):
        print("parent")

class child(parent):
    def show(self):
        print("child")

c1 =  child()
c1.show()
c1.display()
