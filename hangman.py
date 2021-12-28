import random

def run():
    with open("./data.txt", "r", encoding = "utf-8") as d:
        words = [word for word in d]

    j = random.randint(0,170)
    for i, words in enumerate(words):
        if i == j:
            word = words
    l = len(word)
    print(l*" _ ")

if __name__ == '__main__':
    run()