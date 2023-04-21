#write a Python program that finds the Greatest Common Divisor (GCD) of two numbers. 
# Your program should take two input numbers from the user, and use a function named 'gcd' to find the GCD of those two numbers. 
# Your program should then print out the GCD of the two numbers as the output.

def gcd(a,b):
  fact=0
  if (a==0 and b>0):
    fact=b
  if (a>0 and b==0):
    fact=a
  if (a>0 and b>0):
    for i in range(1,min(a,b)+1):
      if (a%i==0 and b%i==0):
        fact=i
  return fact
print("Enter 2 numbers to find the Greatest Common Div")
a=int(input())
b=int(input())
print(gcd(a,b))