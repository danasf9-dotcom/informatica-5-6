def main():
    spain = input("Spain goals: ")
    argentina = input("Argentina goals: ")

    if spain > argentina:
       print("Spain is the winner!")
    elif argentina > spain:
        print("Argentina is the winner!")
    else:
        print("It´s a tie.")

    print("gg")

if __name__ == "__main__":
    main()
