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
      

def run():
     s, word = size()
     print("\nGuess the word!\n")
     
     unders = s*"_" + "\n"
     print(unders)
     
     letters = list(unders)

     while unders != word:
        l = input("\nEnter a letter: ")
        for i in range(0,s):
            if l == word[i]:
                letters[i] = l         
        os.system("clear")
        unders = "".join(letters)
        print("\nGuess the word!\n")
        print(unders.upper())
     
        
     
if __name__ == '__main__':
    run()