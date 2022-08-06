import random
import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def check(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print("did you mean ",get_close_matches(word, data.keys())[0])
        if(input("If yes press y or if no press any key ")=="y"):
            return(data[get_close_matches(word, data.keys())[0]])
        else:
            return("no such word found! please try something else")
    else:
        return("no such word found! please try something else")


def hangman():
    data_key = list(data.keys())
    data_key = [ x for x in data_key if " " not in x ]
    word = random.choice(data_key)
    validLetters = 'abcdefghijklmnopqrstuvwxyz'
    print("valid Letters for this game are:", end=" ")
    for x in validLetters:
        print(x, end=" ")
    print("\n")
    turns = 10
    guessmade = ''

    h = int(len(word)/4)

    for x in range(h):
        ran_ind = random.randint(0,len(word)-1)
        guessmade = guessmade + word[ran_ind]

    while len(word) > 0:
        missed = 0
        main = ""
        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "
        if main == word:
            print(main)
            print("You win!")
            break

        print("Guess the word:" , main)
        guess = input()

        if guess in validLetters:
            guessmade = guessmade + guess
        else:
            print("Enter a valid character")
            guess = input()

        if guess not in word:
            turns = turns - 1
            if turns == 9:
                print("9 turns left")
                print("  --------  ")
            if turns == 8:
                print("8 turns left")
                print("  --------  ")
                print("     O      ")
            if turns == 7:
                print("7 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
            if turns == 6:
                print("6 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            if turns == 5:
                print("5 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 4:
                print("4 turns left")
                print("  --------  ")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 3:
                print("3 turns left")
                print("  --------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if turns == 2:
                print("2 turns left")
                print("  --------  ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            if turns == 1:
                print("1 turns left")
                print("Last breaths counting, Take care!")
                print("  --------  ")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")
            if turns == 0:
                print("You loose")
                print("You let a kind man die")
                print("  --------  ")
                print("     O_|    ")
                print("    /|\      ")
                print("    / \     ")
                print("\ncorrect word is", word)
                break
    output = check(word)
    i=1
    if type(output) == list:
        print("\ndictionary meaning of", word, "is ")
        for x in range(len(output)):
            print("%(n)s. %(m)s" % {'n': i, 'm': output[x]})
            i=i+1
    else:
        print("%(n)s. %(m)s" % {'n': i, 'm': output})

print("\n********************************************************")
name = input("Enter your name ")
print("\n********************************************************\n")
print("Welcome" , name, "\n")
# print("\n")
print("try to guess the word in less than 10 attempts\n")
hangman()
print()
