import random
def main():
    guessing(get_level())
def get_level():
    while True:
        try:
            level = int(input("Enter The Level: "))
            if level <= 0:
                continue
            else:
                return level
        except:
            pass

def guessing(level):
    number = random.randint(1, level)
    while True:
        try:
            guess = int(input("Guess The Number: "))
            if guess < number :
                print("Too small!")
            if guess > number :
                print("Too large!")
            if guess == number:
                print("Just right!")
                break
        except:
            pass
if __name__ == "__main__":
     main()




