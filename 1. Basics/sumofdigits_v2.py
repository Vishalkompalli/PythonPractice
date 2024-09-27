num=int(input("Enter the number: "))
sum=0
while(num>0):
    sum=sum + num%10
    num=num//10
print("Sum of digits: ",sum)

#https://www.geeksforgeeks.org/python-program-for-sum-the-digits-of-a-given-number/