num = int(input("Enter a number: "))
degree = 0
result = 1 # 2^0 = 1

while result < num:
    result *= 2
    degree += 1

if result == num:
    print(f" The degree of 2 for {num} is: {degree}")
else:
    print(f"{num} is not a power of 2")
