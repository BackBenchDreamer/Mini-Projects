import random

def RInt(a, b):
    return random.randint(a, b)

def Choice(a, b):
    return a if RInt(0, 1) else b

def Split(l, mode):
    if mode == 3:  # For Alphanumeric with Symbols
        while True:
            split1 = random.randint(0, l)
            split2 = random.randint(split1, l)

            x = split1
            y = split2 - split1
            z = l - split2

            if x != y != z:  # Ensure all three parts are different
                return x, y, z

    if mode == 2:  # For Alphanumeric
        while True:
            split1 = random.randint(0, l)

            x = split1
            y = l - split1

            if x != y:  # Ensure the two parts are different
                return x, y

    return l  # For Alphabets only, return the length

def Rando(length1, length2=None, length3=None):
    # Initialize password string
    password = ""

    # Random alphabets
    for _ in range(length1):
        password += chr(Choice(RInt(65, 90), RInt(97, 122)))  # Randomly choose between uppercase and lowercase letters

    # Random numbers (if applicable)
    if length2 is not None:
        for _ in range(length2):
            password += str(RInt(0, 9))  # Add random digits

    # Random symbols (if applicable)
    if length3 is not None:
        for _ in range(length3):
            password += chr(RInt(33, 47))  # Add random symbols

    return password

# Main part of the program
choice = int(input("1. Alphabets\n2. Alphanumeric\n3. Alphanumeric with Symbols\nEnter your choice: "))
l = int(input("Enter length of the password: "))

# Generate password based on user's choice
if choice == 1:
    # Only alphabets
    password = Rando(Split(l, choice))
elif choice == 2:
    # Alphanumeric
    length1, length2 = Split(l, choice)
    password = Rando(length1, length2)
elif choice == 3:
    # Alphanumeric with symbols
    length1, length2, length3 = Split(l, choice)
    password = Rando(length1, length2, length3)

print("Your password is:", password)
