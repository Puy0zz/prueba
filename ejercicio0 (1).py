with open("blackcat.txt","r") as file:
    line = file.readlines()
    #print(line)
a= 0
e=0
i= 0
o=0
u=0
for p in line:
    for t in p:
        if t == "a" or t=="A":
            a += 1
        elif t == "e" or t=="E":
            e += 1
        elif t == "i" or t == "I":
            i += 1
        elif t == "o" or t=="O":
            o += 1
        elif t == "u" or t=="U":
            u += 1


print(a,e,i,o,u)
    
