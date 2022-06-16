print("Welcome to my General Knowledge quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("How many time Zones are there in Russia ? ")
if answer.lower() == "two":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("How many valves does the heart have ? ")
if answer.lower() == "four":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does IPA stand for ? ")
if answer.lower() == "indian pale ale":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is the slang name for 'New York City' used by local ? ")
if answer.lower() == "gotham":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Which artist painted the ceiling of the Sistine chapel in Rome ? ")
if answer.lower() == "michelanglo":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What's the smallest country in the world ? ")
if answer.lower() == "the vatican":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What's the capital of Canada ? ")
if answer.lower() == "ottawa":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Name the longest river in the World ? ")
if answer.lower() == "the nile":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")



print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 8) * 100) + "%.")
