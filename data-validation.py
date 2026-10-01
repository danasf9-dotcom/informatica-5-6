def main():
    not_validated = True # Initialization

    while not_validated: # Condition
        try:
            number = int(input("Enter a number between 1 and 10:"))
            if 1 <= number <= 10:
                print("Success!")
                not_validated = False # -> break
        except ValueError:
            print("You must enter a number between 1 and 10.")


    while True:
        try:
            name = input("Enter your name: ")
            f_letter = name[0]
            print("Name stored successfully.")
            break
        except IndexError:
            print("You MUST enter your name.")

if __name__ == "__main__":
   main()
