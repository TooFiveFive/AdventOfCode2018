class Input:
    def __init__(self,before,op,after):
        self.before = before
        self.op = op
        self.after = after
class Ops:
    def __init__(self, data):
        out = []
        for d in data:
            outi = 0
            outi += 1 if self.addr(d) else 0
            outi += 1 if self.addi(d) else 0
            outi += 1 if self.mulr(d) else 0
            if outi < 3:
                outi += 1 if self.muli(d) else 0
            if outi < 3:
                outi += 1 if self.banr(d) else 0
            if outi < 3:
                outi += 1 if self.bani(d) else 0
            if outi < 3:
                outi += 1 if self.borr(d) else 0
            if outi < 3:
                outi += 1 if self.bori(d) else 0
            if outi < 3:
                outi += 1 if self.setr(d) else 0
            if outi < 3:
                outi += 1 if self.seti(d) else 0
            if outi < 3:
                outi += 1 if self.gtir(d) else 0
            if outi < 3:
                outi += 1 if self.gtri(d) else 0
            if outi < 3:
                outi += 1 if self.gtrr(d) else 0
            if outi < 3:
                outi += 1 if self.eqir(d) else 0
            if outi < 3:
                outi += 1 if self.eqri(d) else 0
            if outi < 3:
                outi += 1 if self.eqrr(d) else 0
            if outi >= 3:
                out.append(True)
            else:
                out.append(False)
            # print(outi)
        self.out = out
    def count(self):
        return len([o for o in self.out if o == True])
    def addr(self,d):
        if d.after[d.op[3]] == (d.before[d.op[1]]+d.before[d.op[2]]):
            return True
        else:
            return False
    def addi(self,d):
        if d.after[d.op[3]] == (d.before[d.op[1]]+d.op[2]):
            return True
        else:
            return False
    def mulr(self,d):
        if d.after[d.op[3]] == (d.before[d.op[1]]*d.before[d.op[2]]):
            return True
        else:
            return False
    def muli(self,d):
        if d.after[d.op[3]] == (d.before[d.op[1]]*d.op[2]):
            return True
        else:
            return False
    def banr(self,d):
        if d.after[d.op[3]] == (d.before[d.op[1]]&d.before[d.op[2]]):
            return True
        else:
            return False
    def bani(self,d):
        if d.after[d.op[3]] == (d.before[d.op[1]]&d.op[2]):
            return True
        else:
            return False
    def borr(self,d):
        if d.after[d.op[3]] == (d.before[d.op[1]]|d.before[d.op[2]]):
            return True
        else:
            return False
    def bori(self,d):
        if d.after[d.op[3]] == (d.before[d.op[1]]|d.op[2]):
            return True
        else:
            return False
    def setr(self,d):
        if d.after[d.op[3]] == d.before[d.op[1]]:
            return True
        else:
            return False
    def seti(self,d):
        if d.after[d.op[3]] == d.op[1]:
            return True
        else:
            return False
    def gtir(self,d):
        if d.after[d.op[3]] == int(d.op[1] > d.before[d.op[2]]):
            return True
        else:
            return False
    def gtri(self,d):
        if d.after[d.op[3]] == int(d.before[d.op[1]] > d.op[2]):
            return True
        else:
            return False
    def gtrr(self,d):
        if d.after[d.op[3]] == int(d.before[d.op[1]] > d.before[d.op[2]]):
            return True
        else:
            return False
    def eqir(self,d):
        if d.after[d.op[3]] == int(d.op[1] == d.before[d.op[2]]):
            return True
        else:
            return False
    def eqri(self,d):
        if d.after[d.op[3]] == int(d.before[d.op[1]] == d.op[2]):
            return True
        else:
            return False
    def eqrr(self,d):
        if d.after[d.op[3]] == int(d.before[d.op[1]] == d.before[d.op[2]]):
            return True
        else:
            return False
inputs = []
with open("in.txt") as file:
    b = []
    for i,v in enumerate(file):
        if len(b) == 3:
            inputs.append(Input(b[0],b[1],b[2]))
            b = []
        if i < 3188 and v != "\n":
            if v[0] == "B":
                b.append(list(map(int,v[9:-2].split(", "))))
            elif v[0] == "A":
                b.append(list(map(int,v[9:-2].split(", "))))
            else:
                b.append(list(map(int,v.split(" "))))
# [print(i.before) for i in inputs]
ops = Ops(inputs)
print(ops.out)
print(ops.count())