import random

#1- Select random value
list1 = [7, 6, 2, 1]
print(random.choice(list1))

#2- Generates a random number within a time interval
r1 = random.randint(5, 15)
print(r1)

#3- Select a random string
name = "Python Developer"
r2 = random.choice(name)
print(r2)

#4- Select more random values
print(random.sample(list1, 2))
print(random.sample(list1, 3))
s = "Hello world!"
print(random.sample(s, 2))

#5- Raffle Program
done = False
while not done:
    print("What do you want to do?")
    print("1- Raffle a number")
    print("2- Exit")

    choice = input(">")
    if choice == "1":
        print("Guess a number from 1 to 10.")
        number = int(input("Enter a number from 1 to 10.\n"))
        result = random.randint(1, 10)
        if number == result:
            print("You guessed the number!")
        else:
            print(f"Try again... The number drawn was{result}")
    elif choice == "2":
        done = True
    else:
        print("Invalid option, choce the option 1 or option 2")
