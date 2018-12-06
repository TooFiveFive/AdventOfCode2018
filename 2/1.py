file = open("in.txt")

lines = file.readlines()
two = 0
three = 0
for l in lines:
    for c in l:
        acc = 0
        if l.count(c) == 2:
            two += 1
            break
    for c in l:
        acc = 0
        if l.count(c) == 3:
            three += 1
            break


print(two*three)
