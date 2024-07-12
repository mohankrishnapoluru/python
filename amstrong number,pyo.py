num=int(input("enter anumber:"))
temp=num
sum=0
while(temp>0):
    digit=temp%10
    sum+=digit**3
    temp=temp//10
if num==sum:
    print(num,"it is a ams")
else:
    print(num,"it is not ams")
