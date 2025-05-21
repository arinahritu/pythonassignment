
# #Conditional Statement
# #1.Largest among Three Numbers: Write a Python program that takes three numbers as input and prints out the largest among them.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a>=b and a>=c:
    print("a is the largest number")
elif b>=a and b>=c:
    print("b is the largest number")
else:
    print("c is the largest number")

# # 2. Write a Python program that takes the coordinates (x, y) of a point as input and prints out which quadrant it belongs to (1st, 2nd, 3rd, or 4th).

x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))

if x > 0 and y > 0:
    print("The point is in the 1st quadrant.")
elif x < 0 and y > 0:
    print("The point is in the 2nd quadrant.")
elif x < 0 and y < 0:
    print("The point is in the 3rd quadrant.") 
elif x > 0 and y < 0:
    print("The point is in the 4th quadrant.")  

# #3. Age Classifier: Write a Python program that takes a person's age as input and prints out whether they are an infant (0-1), toddler (2-3), child (4-12), teenager (13-19), adult (20+).

age=int(input("Enter your age: "))

if age>=0:
    if age <= 1:
        print("You are an infant.")
    elif age <= 3:
        print("You are a toddler.")
    elif age <= 12:
        print("You are a child.")
    elif age <= 19:
        print("You are a teenage.")
    else:
        print("You are an adult.")
else:
    print("Invalid age")


# #4.Write a Python program that takes a person's height (in meters) and weight (in kilograms) as input and calculates their Body Mass Index (BMI). Print out their BMI and a message indicating whether they are underweight (<18.5), normal (18.5-24.9), overweight (25-29.9), or obese (>=30).

height = float(input("Enter the height in meters: "))
weight = float(input("Enter the weight in kilograms: "))

bmi = weight / (height ** 2)
print("Your BMI is",bmi)

if bmi < 18.5:
    print ("underweight")
elif 18.5 <= bmi <= 24.9:
    print ("normal")
elif 25 <= bmi <= 29.9:
    print ("overweight")
else:
    print("obese")

# #5. Write a Python program that takes a temperature input in Celsius and converts it to Fahrenheit if the temperature is above 0°C, or to Kelvin if the temperature is below 0°C.

celsius = float(input("Enter temperature in Celsius: "))

if celsius > 0:
    fahrenheit = (celsius * 9/5) + 32
    print("Temparature is convert to fahrenheit",fahrenheit,"F")
elif celsius < 0:
    kelvin = celsius + 273.15
    print("Temparature is convert to kelvin",kelvin,"K")
else:
    print("0 is equal to 32F and 273.15K")

#Simple Calculator: Input two numbers and an operator (+, -, *, /).Use if-elif to perform the operation and print the result. Handle division by zero using conditions.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == '+':
    result = num1 + num2
    print("Result: ", result)
elif operator == '-':
    result = num1 - num2
    print("Result: ", result)
elif operator == '*':
    result = num1 * num2
    print("Result: ", result)
elif operator == '/':
    if num2 != 0:  # Check for division by zero
        result = num1 / num2
        print("Result: ", result)
    else:
        print("Error")
else:
    print("Invalid operator entered!")

#Loop
#1.FizzBuzz: Write a Python program that prints the numbers from 1 to 100. But for multiples of three, print "Fizz" instead of the number, and for the multiples of five, print "Buzz". For numbers that are multiples of both three and five, print "FizzBuzz" using a for loop.
for num in range(1, 101): 
    if num % 3 == 0 and num % 5 == 0:
        print(num,"FizzBuzz")
    elif num % 3 == 0:  
        print(num,"Fizz")
    elif num % 5 == 0:
        print(num,"Buzz")
    #else:
       # print(num)
