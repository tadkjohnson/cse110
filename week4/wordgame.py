# i have added an array of words to pick from, mulitple lengths of words, and it counts how many trys it takes one to guess the word 


import random
initial = "no"
guess = ""
picks = ["dreams", "choice", "sunday", "temple", "gospel", "joseph", "risen", "scripture", "bible", "spirit", "holyness", "apostle", "bishop", "callings", "sacrament", "priesthood"]


initial = input("want to play a word game where I give you a hint, and you guess the word yes/no? ").lower()

if initial == "no":
    print("maybe next time we can play Global Thermalnuclear War.")

if initial != "no":
    answer = random.choice(picks).upper()
    print("I will give you the length of a word. ", len(answer), "how many trys will it take for you to guess it?")
    print("_" *len(answer))
#    print(f"{answer}")
    attempts=0

    while  guess != answer: 
        guess = input(f"The word you need to figure out is, {len(answer)} long. ").upper()
        print(f"Take another guess, what {len(answer)} letter word do you think it is? ")

        attempts +=1
        if len(guess) != len(answer):
            print(f"enter a new guess try for a word that is {len(answer)} long.")
        elif guess == answer: 
            print(f"You guessed {answer} Congrates!!! ")
            print(f"Got it! It took you {attempts} times,  Next time try to do it in less trys?")
    
        else:
            result =[]
            for i in range(len(answer)):
                if guess[i] == answer[i]:
                    result.append(guess[i])
                else:
                    result.append("_ ")
                
            for i in range(len(answer)):
                if result[i] == "_ ":
                    if guess[i] in answer:
                        matched_letter = sum(1 for j in range(len(answer))
                                             if guess[j] == guess[i] and result[j] == guess[j])
                        total_in_secret = answer.count(guess[i])
                        if matched_letter < total_in_secret:
                            result[i] = guess[i].lower()
                        else:
                            result[i] = "_ "
            print(" ".join(result))
else: 
        print("go watch 1983's movie titled WarGames, and come back and try agian.")



    
        
        










 
