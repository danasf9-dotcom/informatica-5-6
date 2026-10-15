def main():
     largest("numbers.txt")
def largest(file):
    number_list = []
    with open(file) as number_file:
        for number in number_file:
            number = number.replace("\n","")
            number_list.append(int(number))

    print(max(number_list))

if __name__ == "__main__":
   main()

