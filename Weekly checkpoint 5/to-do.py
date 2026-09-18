def main():
    tasks = [] # Empty list

    while True:
        print(f"Tasks to do: {len(tasks)}")
        print(tasks)
        command = input("What do you want to do? (add, complete, exit): ")
        if command == "add":
           new_task = input("Enter new task: ")
           tasks.append(new_task)
        elif command == "Complete":
            comp_task = input("Which task did you complete?: ")
            tasks.remove(comp_task)
        elif command == "exit":
            print("Bye Bye!")
            break


if __name__ == "__main__":
   main()
