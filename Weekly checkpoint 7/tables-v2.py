def main():
   valid_nums = []
   for i in range(1,11):
      valid_nums.append(str(i))

   while True:
      times_table = input("Enter the times tables you would like to be tested on or exit: ").lower().strip()

      if times_table == "exit":
         break

      elif times_table in valid_nums:
        max_value = int(input("Enter maximum value for the times table: "))

        print(f"Here is your quiz on the {times_table} times table")

        for x in range (1, max_value + 1):
            answer = x * int(times_table)
            print(f"{x} times {times_table} is ") #{answer} if you want to show the answer
            user_answer = int(input("Answer: "))
            if user_answer == answer:
               print("Correct!")
            else:
               print("Incorrect")
      else:
         print("Invalid command.")


if __name__=="__main__":
   main()
