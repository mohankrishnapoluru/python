num=int(input("enter anumbr"))
factor=[]
for i in range(1,num+1):
    if num%i==0:
        factor.append(i)
print("factor of","num",factor)
