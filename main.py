# Defining the menu and option selection
def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")
        choice = input("Please enter an option: ")
        # Selection of choices for the user
        # 1 makes use of the encode() function
        if choice == "1":
            password = input("Please enter your password to encode: ")
            encode(password)
            print("Your password has been encoded and stored!\n")
        # 2 will be the decode function to undo the encoding
        elif choice == "2":
            print(f"The encoded password is {encode(password)} , and the original password is {decode(encoded_password)}.")
        # Ends the program
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")


def encode(password):
    # Stores "encoded_password" as an empty string variable
    encoded_password = ""
    # Converts the password string into an integer.
    # Each individual digit in the password will be added by 3, then % by 10.
    # % by 10 ensures the new digit remains a single digit. ex * (8+3) % 10 = 1 *
    for digit in password:
        new_digit = str((int(digit) + 3) % 10)
        encoded_password += new_digit
    return encoded_password

def decode(new_password):
    decoded_password = ""
    length = len(new_password)
    for i in range(0, length):  # Loops from 0 to length of password
        decoded_num = (int(new_password[i]) - 3) % 10  # If a negative value, % equation allows for the original value to be gained
        decoded_password += str(decoded_num)  # Converts value to string, and adds to empty variable
    return new_password


if __name__ == '__main__':
    main()
