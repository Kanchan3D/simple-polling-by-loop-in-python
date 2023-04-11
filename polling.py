y=0
n=0
print("\t\tDo you find python easy")
print("\t\tStart the polling")
for i in range(5):
    s=str(input("\t\ttselect your option y/n.."))
    if(s=='y'):
        y=y+1
    else:
        n=n+1
print("\t\ttotal no. of yes are",y)
print("\t\ttotal no. of no are",n)