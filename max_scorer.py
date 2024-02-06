class player:
    def __init__(self,name,city,match,runs,wicket):
        self.pname=name
        self.pcity=city
        self.pmatches=match
        self.pruns=runs
        self.pwickets=wicket
    def player_details(self):
        print(self.pname)
        print(self.pcity)
        print(self.pmatches)
        print(self.pruns)
        print(self.pwickets)
class Team:
    def __init__(self,no):
        self.NOP=no
        self.l=[]
        for i in range(self.NOP):
            name=input("enter player name:")
            city=input("enter player city:")
            matches=int(input("enter player matches:"))
            runs=int(input("enter player runs:"))
            wickets=int(input("enter player wickets:"))
            player_object=player(name,city,matches,runs,wickets)
            self.l.append(player_object)
    def max_run_scoreer(self):
        mxo=self.l[0]
        for j in self.l:
            if j.pruns>mxo.pruns:
                mxo=j
        return mxo.pname
    def min_wicket_taker(self):
        mno=self.l[0]
        for i in self.l:
            if i.pwickets<mno.pwickets:
                mno=i
        return mno.pname
India=Team(2)
print("highest run scorer is",India.max_run_scoreer())
print("minimum wicket taker is",India.min_wicket_taker())






