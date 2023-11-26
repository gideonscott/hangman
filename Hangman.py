word = "test" 
lives = 8 
currentcorrect=["_" for letter in word]
print(currentcorrect)
completed=False
while lives > 0 and completed==False:
    guess = input("input a letter: ")
    if guess in word:
        print("correct guess")
        for i in range(len(word)):
            if word[i]==guess:
                currentcorrect[i] = word[i]
        if "_" not in currentcorrect:
            completed=True     
        print(currentcorrect)
    else:
        lives=lives-1
        print("incorrect, try again")
        print("lives: "+ str(lives))
if completed == True:
    print("you win")
if completed == False:
    print("you lose get good kid")



