def main():
    # planet = input("Planet: ")

    # #separation
    # print("Hello", planet)

    # #concatenation
    # print("Hello " + planet)

    # #Formatted Strings
    # print(f"Hello {planet}")

    # #Ending
    # print("Hello", end=" ")
    # print(planet)

    name = input("What is your name? ").strip().title()
    color = input("Tell me a color: ").strip().lower()
    adj = input("Give me an adjective: ").strip().lower()
    goal = input("A goal you want to achieve: ").strip().lower()

    print(f"Hello, {name}!")
    print()

    print("This is your story:")
    print(f"At dawn the sky turned {color}, and the air felt {adj}. I decide today I will finally {goal}.")

    print("This is your story:")
    print(f"At dawn the sky turned {color}, and the air felt {adj}. I decide today I will finally {goal}. ".upper())


if __name__== "__main__":
    main()
