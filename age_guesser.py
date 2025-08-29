import random

def greet():
    print("Hi! I am going to guess your age.")
    name = input("First, tell me your name.\n")
    return name

def guess_age(name, guess_count):
    if guess_count >= 6:
        print("Shucks! I could not guess your age.")
        return
    age = random.randint(15,30)
    print("Well, "+name+", I think you are "+str(age)+" years old!")
    answer = input("Did I guess correctly? (Y/N)\t")
    if answer.lower() == "y":
        print("Alas! Success! "+name+" is "+str(age)+" years old.")
        return
    else:
        print("Rats!")
        guess_age(name, guess_count+1)

def main():
    guess_age(greet(), 1)
    return

if __name__ == '__main__':
    main()
