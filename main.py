import random
import os

BLACK = "\u001b[40m"
GREEN = "\u001b[42m"
YELLOW = "\u001b[43m"
RESET = "\u001b[0m"

with open("words.txt", "r") as file:
	words = file.readlines()
for i, word in enumerate(words):
	words[i] = word.replace("\n", "").upper()
word = random.choice(words).upper()

Guessing = True
history = "You word is " + str(len(word)) + " letters long!\n"
print(history)
while Guessing:
	out = ""
	correct = 0
	data = {"correct": {}, "similar": {}, "total": {}}
	guess = input("Guess:\n").upper()
	if len(guess) == len(word) and guess in words:
		for i, letter in enumerate(guess):
			data["total"][letter] = word.count(letter)
			if word[i] == letter:
				if letter in data["correct"]:
					data["correct"][letter] += 1
				else:
					data["correct"][letter] = 1
				correct += 1
			if letter in data["correct"]:
				data["similar"][letter] = word.count(letter) - data["correct"][letter]
			else:
				data["similar"][letter] = word.count(letter)
		for i, letter in enumerate(guess):
			if word[i] == letter and data["correct"][letter] > 0:
				out += GREEN + letter
				data["correct"][letter] -= 1
			elif letter in word and data["similar"][letter] > 0:
				out += YELLOW + letter
				data["similar"][letter] -= 1
			else:
				out += BLACK + letter
		out += RESET
		history += out + "\n"
		os.system('cls' if os.name == 'nt' else 'clear')
		print(history)
	elif len(guess) != len(word):
		os.system('cls' if os.name == 'nt' else 'clear')
		print(history + "\nYou must make a guess that is " + str(len(word)) + " letters long!")
	else:
		os.system('cls' if os.name == 'nt' else 'clear')
		print(history + "\nYour guess wasn't found in the word list!")
	if correct == len(word):
		Guessing = False
		print("You Won!")
