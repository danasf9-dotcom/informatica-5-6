def main():
    # Read a file
    with open("Sample.txt") as new_file:
        content = new_file.read()
        print(content)

    # Turn file content into a list
    count = 0
    with open("Sample.txt") as hoco_week:
        for line in hoco_week:
            line = line.replace("\n","")
            count += 1
            print(f"Day {count}: {line}")

if __name__ == "__main__":
   main()
