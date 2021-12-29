import random

def read_words(): #read data
    with open("./data.txt", "r", encoding = "utf-8") as d:
        list_words = [word for word in d]
    return list_words

def size(): #Obtain the number of letters of just a word
    words = read_words()
    j = random.randint(0,170)
    l = len(words[j]) - 1
    return l
      

def run():
     print(size()*"_ ")
     
    #with open("./data.txt", "r", encoding = "utf-8") as d:
     #   words = [word() for word in d]

    #j = random.randint(0,170)
    #for i, words in enumerate(words):
    #    if i == j:
    #        word = words
    #l = len(word)
    #print(l*" _ ")

if __name__ == '__main__':
    run()