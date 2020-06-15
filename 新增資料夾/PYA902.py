f = open("read.txt")
# TODO
with f as data:
    b=f.read()
    a=b.split(" ")
    c=0
    for i in range(len(a)):
        c+=eval(a[i])
print(c)