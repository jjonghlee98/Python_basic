number = int(input("Enter a number: "))

for i in range(1, number+1):
    print("*" * i)
print()

for i in range(1, number+1):
    print((" " * (number - i))+("*" * (2 * i - 1)))
print()

print(number[::-1])



for i in range(1, number+1):
    print((' ' * (number-i)) + ('*' * (i*2-1)))
print()    
