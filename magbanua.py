import pyfiglet

ascii_art1 = pyfiglet.figlet_format("-------------")
ascii_art2 = pyfiglet.figlet_format("WELCOME TO PERPETUAL ASSISTANT!")
ascii_art3 = pyfiglet.figlet_format("-------------")
ascii_art4 = pyfiglet.figlet_format("!--*--*--*--!")
ascii_art5 = pyfiglet.figlet_format("*GUESSING NUMBER GAME!*")
ascii_art6 = pyfiglet.figlet_format("!--*--*--*--!")
ascii_art7 = pyfiglet.figlet_format("-----The End!-----")

print(ascii_art1)
print(ascii_art2)
print(ascii_art3)


num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

sum_result = num1 + num2 

print(f"The sum of {num1} and {num2} is = {sum_result}")



print(ascii_art4)


print(ascii_art5)

secret_number = 40
while True:
    try:
        guess = int(input("Enter Your guess "))
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too High! Try again.")
        else:
            print("UY TAMA NAYSWAN!")
            break
    except ValueError:
        print("Please enter a valid number.") 


print(ascii_art6)

print(ascii_art7)



