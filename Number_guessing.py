from random import randint


secret_number = randint(1, 100)
print("DEBUG: secret number =", secret_number)


while True:
    try:
        user_guess = int(input("Enter an Number between 1 to 100: "))
    except ValueError:
        print("Enter an vaild value")
        continue
    
    if user_guess == secret_number:
        print("Congrates🙌,You have won")
        break
    elif user_guess > secret_number:
        print("Too high!!")
    elif user_guess < secret_number:
        print("Too low")

print("Your secret number is ",secret_number)