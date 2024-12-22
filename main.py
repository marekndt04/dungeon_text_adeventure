# function def main that takes name input from user and prints it


def print_skull_logo():
    print(
        """
                 ______
              .-"      "-.
             /            \\
            |              |
            |,  .-.  .-.  ,|
             ) (__/  \\__) (
             /     /\\     \\
      (@_   (_     ^^     _)
 _     ) \\____\\_|IIIIII|_/_________________________
(_)@8@8{}<_____|-IIIIII-|__________________________>
       )_/    \\         /
      (@       `-------`
"""
    )


def main():
    print_skull_logo()
    name = input("What is your name? ")
    print("Hello, " + name + "!")


if __name__ == "__main__":
    main()
