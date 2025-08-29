import random

def greet():
	print("Hi! I am going to guess your age.")
	name = input("First, tell me your name.\n")
	return name

def guess_age(name):
	age = random.randint(15,30)
	print("Well, "+name+", I think you are "+str(age)+" years old!")
	answer = input("Did I guess correctly? (Y/N)\t")
	if answer.lower() == "y":
		print("Alas! Success! "+name+" is "+str(age)+" years old.")
		return
	else:
		print("Rats!")
		guess_age(name)

def main():
	guess_age(greet())
	return

if __name__ == '__main__':
	main()
