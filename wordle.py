import colorama 
from colorama import Fore
import random


from pandas import pandas as pd



data = pd.read_csv("word.csv")
word_choice = data["words"].tolist()
w=random.choice(word_choice)
colorama.init(autoreset=(True))
print(w)
cnt=0
c=0

print("WORDLE:")
print(Fore.RED+"RED is for wrong letter guessed.")
print(Fore.BLUE+"BLUE is for correct letter guessed but at wrong position.")
print(Fore.GREEN+"Green is for correct word guessed and correct position.")
print(Fore.BLACK+"You have 6 tries")
print(Style.RESET_ALL)

for i in range(6):
    s= input("Enter your Word")
    s=s.lower()
    for i in range(5):
        if s[i]==w[i]:
            print(Fore.GREEN+s[i],end="")
            c+=1
            cnt+=1
            if cnt==5:
                break;
        elif s[i] in w:
            print(Fore.BLUE+s[i],end="")
            c+=1
        else:
            print(Fore.RED+s[i],end="")
            c+=1
            
if c==6:
    print("The word is",w)
            
            

