'''Number Pattern - Hollow Pyramid (for loop)
Take an integer n and a symbol input and print a hollow pyramid pattern.'''

n=int(input("Enter the number of rows: "))
symbol=input("Enter the symbol: ")

for i in range(1, n+1):
    print(" " * (n-i),end="")
    for j in range(2*i-1):
        if j ==0 or j==2* i-2 or i==n:
            print(symbol, end="")
        else:
            print(" ", end="")
    print()

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''Prime Number in a Range (for loop)
Take two integers a and b, and print all prime numbers between them. Use nested
loops and conditionals'''

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a > b:
    a, b = b, a

print("Prime numbers between a and b :")

for num in range(a, b + 1):
    if num < 2:
        continue
    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(num, end=" ")
print()
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''Strong Number Checker (while loop)
A number is strong if the sum of factorials of its digits equals the number itself.
Example: 145 → 1! + 4! + 5! = 145.
Take a number as input and check if it is a strong number.'''

num = int(input("Enter a number: "))
original_num = num
sum_fact = 0

while num > 0:
    digit = num % 10  
    num = num // 10
    
    fact = 1
    i = digit
    while i > 1:
        fact *= i
        i -= 1
    
    sum_fact += fact  

if sum_fact == original_num:
    print(original_num,"is a strong number")
else:
    print( original_num,"is not a Strong number")

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''Number to Words Converter (while loop + conditionals)
Input: a positive integer.
Output: Print its digits as words (e.g., 123 → "One Two Three").'''

num = int(input("Enter a positive integer: "))
original_num = num 
result = ""        
position = 1        

if num == 0:
    result = "Zero"

while num > 0:
    digit = num % 10
    num = num // 10   
    
    if digit == 0:
        word = "Zero"
    elif digit == 1:
        word = "One"
    elif digit == 2:
        word = "Two"
    elif digit == 3:
        word = "Three"
    elif digit == 4:
        word = "Four"
    elif digit == 5:
        word = "Five"
    elif digit == 6:
        word = "Six"
    elif digit == 7:
        word = "Seven"
    elif digit == 8:
        word = "Eight"
    elif digit == 9:
        word = "Nine"
    
    
    if position == 1:
        result = word
    else:
        result = word + " " + result
    
    position += 1

print(result)

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''Perfect Number Checker
A number is perfect if the sum of its proper divisors (excluding itself) equals the
number.
Example: 28 → 1 + 2 + 4 + 7 + 14 = 28.
Input a number and check if it's perfect.'''

num = int(input("Enter a positive integer: "))
original_num = num
sum_divisors = 1  
divisor = 2
max_divisor = num // 2  

while divisor <= max_divisor:
    if num % divisor == 0:
        sum_divisors += divisor
    divisor += 1

if sum_divisors == original_num and original_num != 0:
    print(original_num," is a perfect number!")
else:
    print(original_num," is not a perfect number.")

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''Digital Root Calculator
Take a number as input. Continuously sum its digits until only one digit remains.
Example: 9875 → 9+8+7+5=29 → 2+9=11 → 1+1=2.'''
num = int(input("Enter a number: "))
print("Digital root of :",num)

while num > 9:
    # Calculate sum of digits
    sum_digits = 0
    temp = num
    while temp > 0:
        sum_digits += temp % 10
        temp = temp // 10
    
    # Print the current step
    print( num,"'s sum of digits: ",sum_digits)
    num = sum_digits

print("Final digital root: ",num)

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''Binary to Decimal Converter (while loop)
Input: A binary number (e.g., 1101).
Output: Convert it to decimal using only math and conditionals (no built-in
conversion).'''

binary = input("Enter binary: ")
decimal = 0
power = 1  # Starts at 2⁰ = 1

# Process digits right-to-left using math
temp = int(binary)
while temp > 0:
    last_digit = temp % 10
    if last_digit == 1:
        decimal += power
    elif last_digit > 1:
        print("Invalid binary number!")
        exit()
    power *= 2
    temp = temp // 10

print("Decimal:", decimal)

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''Frequency of Each Digit (while loop + conditionals)
Input: A number like 1223334444.
Output: Count and print how many times each digit (0–9) appears.'''
num = int(input("Enter a number: "))
original_num = num 

count0 = count1 = count2 = count3 = count4 = 0
count5 = count6 = count7 = count8 = count9 = 0

if num == 0:
    count0 = 1

while num > 0:
    digit = num % 10 
    num = num // 10 
    
    if digit == 0:
        count0 += 1
    elif digit == 1:
        count1 += 1
    elif digit == 2:
        count2 += 1
    elif digit == 3:
        count3 += 1
    elif digit == 4:
        count4 += 1
    elif digit == 5:
        count5 += 1
    elif digit == 6:
        count6 += 1
    elif digit == 7:
        count7 += 1
    elif digit == 8:
        count8 += 1
    elif digit == 9:
        count9 += 1

print(f"Digit counts for {original_num}:")
for digit in range(10):
    count = 0
    if digit == 0:
        count = count0
    elif digit == 1:
        count = count1
    elif digit == 2:
        count = count2
    elif digit == 3:
        count = count3
    elif digit == 4:
        count = count4
    elif digit == 5:
        count = count5
    elif digit == 6:
        count = count6
    elif digit == 7:
        count = count7
    elif digit == 8:
        count = count8
    elif digit == 9:
        count = count9
    
    if count > 0:
        print("Digit", digit,"is",count,"times")

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''Armstrong Numbers in a Range (for loop)
Take two numbers as input and print all Armstrong numbers between them.'''

start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

print("Armstrong numbers between ",start," and ",end)

for num in range(start, end + 1):
    temp = num
    digits = 0
    while temp > 0:
        digits += 1
        temp = temp // 10

    temp = num
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum += digit ** digits
        temp = temp // 10
    
    if sum == num:
        print(num)


