import random 

number = random.randint(1,9)
chances = 5

guess= int(input("please guess a number between 1 to 9 "))
chances=chances-1

while chances < 5:
    if guess > number:
        chances=chances-1
        guess = int(input("guess a lower number: "))

    elif guess < number :
        chances=chances-1
        guess = int(input("guess a number higer: "))

    elif guess == number:
        print("Congratulation YOU WON!!!")
        break
    if chances == 0 :
        print("you lose!! the number was",number)
        break
    