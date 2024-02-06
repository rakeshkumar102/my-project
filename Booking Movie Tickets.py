def singleTon(arg):
    d={}
    print(arg)
    def inner():
        if arg not  in d:
           MultiplexObject=arg()
           d[arg]=MultiplexObject
        return d[arg]
    return inner
@singleTon
class Multiplex:
    def __init__(self):
        self.tickets=500
    def booking(self,n):
        if self.tickets>=n:
            self.tickets-=n
            print(f"booking of {n} tickets")
            print("remaining tickets available",self.tickets)
        else:
            print("in-sufficient tickets")
rakesh=Multiplex()
rakesh.booking(200)
print(rakesh)
raaj=Multiplex()
raaj.booking(200)
print(raaj)
ram=Multiplex()
ram.booking(200)
print(ram)
