def main():
    print("suchi box")

    rating = int(input("rank our service: "))

    if rating > 4.5:
        print("Perfection")
    elif rating > 4:
        print("Excellent")
    elif rating > 3:
        print("Good")
    elif rating > 2:
        print("Fair")
    else:
        print("Poor")

    print("Thank you!")

if __name__ == "__main__":
    main()
