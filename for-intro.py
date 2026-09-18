def main():
    doctrine = ["Faith in the lord jesus christ", "Repentance", "Baptism", "Imposicion de manos", "Perseverar hasta el fin"]

    index = 0

    # while index < len(doctrine): condition
    #   print(doctrine[index])
    #   index += 1 update

    for i in range(len(doctrine)):
        print(f"{i+1} {doctrine[i]}")

if __name__ == "__main__":
   main()

