def are_anagrams(string1, string2):
    string1 = ''.join(c.lower() for c in string1 if c.isalnum())
    string2 = ''.join(c.lower() for c in string2 if c.isalnum())
    return sorted(string1) == sorted(string2)


def hex_to_decimal(hex_string):
    # Convert the hexadecimal string to a list of characters
    hex_chars = list(hex_string.strip().upper())

    # Initialize the decimal value to 0
    decimal_value = 0

    # Iterate over the characters in the hexadecimal string
    for i, char in enumerate(hex_chars):
        # Check if the character is a valid hexadecimal digit
        if char >= '0' and char <= '9':
            value = int(char)
        elif char >= 'A' and char <= 'F':
            value = 10 + (ord(char) - ord('A'))
        else:
            return None

        # Multiply the decimal value by 16 and add the value of the current hexadecimal digit
        decimal_value = (decimal_value << 4) + value

    # Return the decimal value
    return decimal_value

# Read a string from the user
user_input = input("Enter a hexadecimal number: ")

# Check if the string is a valid hexadecimal number
decimal_value = hex_to_decimal(user_input)
if decimal_value is None:
    print("Error: The string is not a valid hexadecimal number.")
else:
    print("The decimal value is:", decimal_value)