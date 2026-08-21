def main():

    transistors = 17.8
    years = int(input("How many years?"))

    transistors *= 2**(years/2)

    print(transistors, "billions")




if __name__ == "__main__":
    main()
