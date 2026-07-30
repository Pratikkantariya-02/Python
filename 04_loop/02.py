n = int(input("Enter number : "))
sum_even = 0

for num in range(1,n+1):
    if num%2==0:
        sum_even +=num
print("Sum of event number is : ",sum_even)

