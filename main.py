num1 = list(map(int, input("Enter the numbers ").split()))
num2 = list(map(int, input("Enter the numbers ").split()))
print(set(num2).issubset(set(num1)))
