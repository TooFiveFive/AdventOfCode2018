class Input:
    def __init__(self,before,op,after):
        self.before = before
        self.op = op
        self.after = after
class Ops:
    opers = ["addr","addi","mulr","muli","banr","bani","borr","bori","setr","seti","gtir","gtri","gtrr","eqir","eqri","eqrr"]
    def set_res(self,data):
        self.res = data
    def do(self,data,action):
        if action == "addr":
            self.regs[data[3]] = self.regs[data[1]]+self.regs[data[2]]
        if action == "addi":
            self.regs[data[3]] = self.regs[data[1]]+data[2]
        if action == "mulr":
            self.regs[data[3]] =  self.regs[data[1]]*self.regs[data[2]]
        if action == "muli":
            self.regs[data[3]] =  self.regs[data[1]]*data[2]
        if action == "banr":
            self.regs[data[3]] =  self.regs[data[1]]&self.regs[data[2]]
        if action == "bani":
            self.regs[data[3]] =  self.regs[data[1]]&data[2]
        if action == "borr":
            self.regs[data[3]] =  self.regs[data[1]]|self.regs[data[2]]
        if action == "bori":
            self.regs[data[3]] =  self.regs[data[1]]|data[2]
        if action == "setr":
            self.regs[data[3]] =  self.regs[data[1]]
        if action == "seti":
            self.regs[data[3]] =  data[1]
        if action == "gtir":
            self.regs[data[3]] =  int(data[1] > self.regs[data[2]])
        if action == "gtri":
            self.regs[data[3]] =  int(self.regs[data[1]] > data[2])
        if action == "gtrr":
            self.regs[data[3]] =  int(self.regs[data[1]] > self.regs[data[2]])
        if action == "eqir":
            self.regs[data[3]] =  int(data[1] == self.regs[data[2]])
        if action == "eqri":
            self.regs[data[3]] =  int(self.regs[data[1]] == data[2])
        if action == "eqrr":
            self.regs[data[3]] =  int(self.regs[data[1]] == self.regs[data[2]])
    def test(self,data):
        self.regs = [0]*4
        for i in data:
            self.do(i,self.res[i[0]])
        print(self.regs)
    def __init__(self, data):
        
        out = []
        for d in data:
            outi = []
            outi.append(1 if self.addr(d) else 0)
            outi.append(1 if self.addi(d) else 0)
            outi.append(1 if self.mulr(d) else 0)
            outi.append(1 if self.muli(d) else 0)
            outi.append(1 if self.banr(d) else 0)
            outi.append(1 if self.bani(d) else 0)
            outi.append(1 if self.borr(d) else 0)
            outi.append(1 if self.bori(d) else 0)
            outi.append(1 if self.setr(d) else 0)
            outi.append(1 if self.seti(d) else 0)
            outi.append(1 if self.gtir(d) else 0)
            outi.append(1 if self.gtri(d) else 0)
            outi.append(1 if self.gtrr(d) else 0)
            outi.append(1 if self.eqir(d) else 0)
            outi.append(1 if self.eqri(d) else 0)
            outi.append(1 if self.eqrr(d) else 0)

            out.append([d.op[0],outi])

            # print(outi)
        self.out = out
    def count(self):
        return len([o for o in self.out if o == True])
    def rets(self):
        r = dict((el,[]) for el in self.opers)
        for i,op in enumerate(self.opers):
            for o in self.out:
                if o[1][i] == 1:
                    r[op].append(True)
                else:
                    r[op].append(False)
        return r
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
ops = Ops(inputs)
rets = ops.rets()
keys = dict((el,[]) for el in ops.opers)
# results = dict((el,"no") for el in range(16))
for i in range(len(ops.out)):
    for key in rets.keys():
        if rets[key][i]:
            keys[key].append(ops.out[i][0])
rd = dict((el,[]) for el in range(16))
print(keys)
for i in range(16):
    l = [0]*16
    for index,key in enumerate(keys.keys()):
        if i in keys[key]:
            l[index] = keys[key].count(i)
    rd[i] = l
print(rd)
kys = list(keys.keys())
results = dict((el,"no") for el in range(16))
for i in range(16):
    mx = (100**100,100**100)
    for index,ii in enumerate(rd[i]):
        mxlocal = 0
        if ii > 0:
            for iii in range(16):
                if rd[iii][index] > 0:
                    mxlocal += 1
            if mxlocal < mx[1]:
                mx = (index,mxlocal)
    results[i] = kys[mx[0]]

print(results)

ops.set_res(results)
print(results)
with open("in.txt") as file:
    data = []
    for i,v in enumerate(file):
        if i >= 3188 and v != "\n":
            data.append(list(map(int,v.split(" "))))
    ops.test(data)