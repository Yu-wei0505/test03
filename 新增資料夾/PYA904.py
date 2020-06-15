data = []
with open("read.txt","r") as file:
    for line in file:
        print(line)
        a=line.strip("\n").split(" ")
        a=(a[0],eval(a[1]),eval(a[2]))
        data.append(a)
name=[data[x][0]for x in range(len(data))]
height=[data[x][1]for x in range(len(data))]
weight=[data[x][2]for x in range(len(data))]
print("Average height: %.2f" % (sum(height)/len(name)))
print("Average weight: %.2f" % (sum(weight)/len(name)))
maxheight=max(height)
maxweight=max(weight)
print("The tallest is %s with %.2fcm" % (name[height.index(maxheight)],maxheight))
print("The heaviest is %s with %.2fkg" % (name[weight.index(maxweight)],maxweight))
