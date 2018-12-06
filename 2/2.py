file = open("in.txt")
lines = file.readlines()
def ans():
    for i, l in enumerate(lines):
        l = l.replace("\n", "")
        for l2 in lines[i+1:]:
            l2 = l2.replace("\n", "")
            acc = 0
            d = 0
            for il in range(len(l)):
                if l[il] == l2[il]:
                    acc += 1
                    if acc == len(l)-1:
                        out = l[:d] + l[d+1:]
                        return out
                else:
                    d = il
print(ans())