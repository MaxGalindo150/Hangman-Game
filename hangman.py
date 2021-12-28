def run():
    with open("./data.txt", "r", encoding = "utf-8") as d:
        words = [word for word in d]
        print(words)

if __name__ == '__main__':
    run()