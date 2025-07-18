def square_number():
    try:
        a = int(input("Enter a number: "))
        print(a ** 2)
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    square_number()
    print("Hello World")






