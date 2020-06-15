# TODO
a=eval(input())
if a%3==0 and a%5==0:
    print("{:d} is a multiple of 3 and 5.".format(a))
elif a%3==0 and a%5!=0:
    print("{:d} is a multiple of 3.".format(a))
elif a%3!=0 and a%5==0:
    print("{:d} is a multiple of 5.".format(a))
else:
    print("{:d} is not a multiple of 3 or 5.".format(a))
     
     



"""
_ is a multiple of 3 and 5.
_ is a multiple of 3.
_ is a multiple of 5.
_ is not a multiple of 3 or 5.
"""