import random
import os

def read_words(): #read data
    with open("./data.txt", "r", encoding = "utf-8") as d:
        list_words = [word for word in d]
    return list_words

def size(): #Obtain the number of letters of just a word
    words = read_words()
    j = random.randint(0,170)
    s = len(words[j]) - 1
    return s, words[j]

def start(): #Welcome to hangman
    return print("\nGuess the word!\n")       

def run():
     s, word = size()
     
     start()
     
     unders = s*"_" + "\n"
     print(unders)
     
     letters = list(unders)
     k = 0
     while k < 6:
        k = k + 1
        l = input("\nEnter a letter: ")
        for i in range(0,s):
            if l == word[i]:
                letters[i] = l         
        os.system("clear")
        unders = "".join(letters)
        start()
        print(unders.upper())
        if unders == word:
            break
     if unders == word:
        print("YES! the word was " + word.upper() + " ;)")       
     else:
        print("UPS! You lose :(")
        
     
if __name__ == '__main__':
    run()