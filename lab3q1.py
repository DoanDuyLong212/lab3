for i in range(1,6):
    print(*range(1,i+1))


def sum_of_numbers():
    while True:
        try:
            n = int(input("Enter number: "))
            if n < 1:
                raise ValueError("Error: The input must be a positive integer.")
            total = 0
            for i in range(1, n + 1):
                total += i
            print("sum is", n, "is", total)
            break
        except ValueError as e:
            print(e)
sum_of_numbers()
