# welcome to Friend Vibes
print(" ***** Welcome to the Friendly Vibes ******")

# intalize counters
total = 0

# ask question
question1 = "Are you confident about yourself?"
print(question1)

while True:
    response = input("Enter yes or no. ")

    if response == "yes":
        total += 10
        break
    elif reponse == "no":
        total += 20
        break
    else:
        print("Incorrect!!! Enter yes or no!")

        while True:
            response = input("Enter yes or no. ")

            if response == "yes":
                total += 10
                stop = True
                break
            elif reponse == "no":
                total += 20
                break
        if stop:
            break
question2 = ("Do you think you like change?")
print(question2)
while True:
    response = input("Enter yes or no. ")

    if response == "yes":
        total += 10
        break
    elif reponse == "no":
        total += 20
        break
    else:
        print("Incorrect!!! Enter yes or no!")

        while True:
            response = input("Enter yes or no. ")

            if response == "yes":
                total += 10
                stop = True
                break
            elif reponse == "no":
                total += 20
                break
        if stop:
            break
question3 = ("Is your favourite season summer?")
while True:
    response = input("Enter yes or no. ")

    if response == "yes":
        total += 10
        break
    elif reponse == "no":
        total += 20
        break
    else:
        print("Incorrect!!! Enter yes or no!")

        while True:
            response = input("Enter yes or no. ")

            if response == "yes":
                total += 10
                stop = True
                break
            elif reponse == "no":
                total += 20
                break
        if stop:
            break
print(question3)
while True:
    response = input("Enter yes or no. ")

    if response == "yes":
        total += 10
        break
    elif reponse == "no":
        total += 20
        break
    else:
        print("Incorrect!!! Enter yes or no!")

        while True:
            response = input("Enter yes or no. ")

            if response == "yes":
                total += 10
                stop = True
                break
            elif reponse == "no":
                total += 20
                break
        if stop:
            break
question4 = ("Is your favourite season Fall?")
print(question4)
while True:
    response = input("Enter yes or no. ")

    if response == "yes":
        total += 10
        break
    elif reponse == "no":
        total += 20
        break
    else:
        print("Incorrect!!! Enter yes or no!")

        while True:
            response = input("Enter yes or no. ")

            if response == "yes":
                total += 10
                stop = True
                break
            elif reponse == "no":
                total += 20
                break
        if stop:
            break
question5 = ("Do you enjoy talking to men more female?")
print(question5)
while True:
    response = input("Enter yes or no. ")

    if response == "yes":
        total += 10
        break
    elif reponse == "no":
        total += 20
        break
    else:
        print("Incorrect!!! Enter yes or no!")

        while True:
            response = input("Enter yes or no. ")

            if response == "yes":
                total += 10
                stop = True
                break
            elif reponse == "no":
                total += 20
                break
        if stop:
            break
print("Your score is " + str(total) + " and you are matched with Kevin.")