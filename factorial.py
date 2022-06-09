def recursive_factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*recursive_factorial(n-1) 
number = int(input("Enter the input : "))
if number < 0:
  print("Factorial does not exist for negative numbers")
else:
  print("The factorial of", number, "is", recursive_factorial(number))
