n = int(input("Enter the Maximum Value to find the sum of odd numbers: "))
sumofodd = 0
start = 1
 
while start <= n:
    if(start % 2 != 0):
        sumofodd = sumofodd + start
    start = start + 1

print("The Sum of Odd Numbers from 1 to {0} = {1}".format(n, sumofodd))
