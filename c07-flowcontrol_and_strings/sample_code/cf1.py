import random

number = random.randint(1,100)

guess = int(input("I'm thinking of a number between 1 and 100. What is it? : "))

if guess == number:
    print('The odds of getting this in the first guess are 1/100.')
    print('Congratulations, you guessed it.')
elif guess < number:
    print('No, it was a little higher than that')
else:
    print('No, it was a little lower than that')

print('Done')
