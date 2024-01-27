def is_anagram():
    while True:
        try:
            str1 = input("Enter the first string: ").strip().lower()
            str2 = input("Enter the second string: ").strip().lower()
            if len(str1) != len(str2):
                raise ValueError("Error: The two strings must have the same length.")
            sorted_str1 = ''.join(sorted(str1))
            sorted_str2 = ''.join(sorted(str2))
            if sorted_str1 == sorted_str2:
                print("The two strings are anagrams.")
            else:
                print("The two strings are not anagrams.")
            break
        except ValueError as e:
            print(e)

# Testing the function
is_anagram()


def hex_to_decimal():
    while True:
        try:
            hex_str = input("Enter a hexadecimal string: ").strip().upper()
            if not all(c in '0123456789ABCDEF' for c in hex_str):
                raise ValueError("Error: The input string must contain only hexadecimal digits.")
            decimal_value = int(hex_str, 16)
            print("The decimal value of the hexadecimal string is:", decimal_value)
            break
        except ValueError as e:
            print(e)

# Testing the function
hex_to_decimal()

    print("The decimal value is:", decimal_value)
