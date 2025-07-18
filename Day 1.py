def square_number():
    while True:
        try:
            a = int(input("Enter a number: "))
            return a ** 2
        except:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    
    square_number()
    print("Hello World")






