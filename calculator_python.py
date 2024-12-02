operator= input ("Enter an operator + / * - ") 
num1 = float(input ("Enter the first number: "))
num2 = float(input ("Enter the second number: "))

if operator == "-":
     result = num1 - num2
     print(f"The result is {result}")

elif operator == "/":

   if num2 == 0:
       print(" Impossible to divide by 0, fix this !!!!")
   
   
   else: 
       result = num1 / num2
       print (f"The result is {result}")

elif operator == "*":
   result = num1 * num2
   print(f"The result is {result}")
elif operator == "+":
   result = num1 + num2
   print(f"The result is {result}")

else: print("Please choose a operator that works")





