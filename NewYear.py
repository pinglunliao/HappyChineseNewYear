import os 
import time
from colorama import Fore, Back
import random

os.system('cls')
colors = list(vars(Fore).values())

filename=["file1.txt","file2.txt", "file3.txt","file4.txt", "file5.txt"]

def animator(filename, delay=1, repeat=10):
	text=[]
	for name in filename:
		with open(name, "r", encoding="utf-8") as f:
			text.append(f.readlines())

	for i in range(repeat):
		for txt in text:
			print(random.choice(colors))
			print("".join(txt))
			# print(Back.LIGHTMAGENTA_EX)
			time.sleep(delay)
			os.system('cls')


animator(filename, delay=0.5, repeat=5)

animator(filename, delay=0.1, repeat=5)

animator(filename, delay=1, repeat=3)