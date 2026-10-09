def main():
   def highest(a, b):
      if a > b:
         highest_num = a
         print(f"The highest number entered is {highest_num}")
   else :
   highest_num = b
   print(f"The highest number entered is {highest_num}")

    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    highest(num1, num2)

   def lower(a, b, c):
      if a < b and a < c:
         lowest_num = a
      elif  b < a and b < c:
         lowest_num = b
      else:
         lowest_num = c
         print(f"lowest number = {lowest_num}")

    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a second number: "))
    num3 = int(input("Enter a  third number: "))
    lower(num1, num2, num3)


if __name__ == "__main__":
   main()
