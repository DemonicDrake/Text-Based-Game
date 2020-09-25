import time
import random
import os

CharacterInfo=[]
char=""
c=0
racesel="none"
classsel="none"
bckgsel="none"
racesel2=""

print("checking for existing character in directory")
try:
    char=open("character.txt","r+")
    print("existing character found")
    c+=1
except:
    print("no character found, skipping to character creation")

if c==0:
    while True:
        print("Character Creation Menu \n")
        print("1. race         selected:",racesel)
        print("2. class        selected:",classsel)
        print("3. background   selected:",bckgsel)
        print("\n enter a number to select an option or press enter if you are finished")
        sel=str(input())
        if sel=="1":
            while True:
                print("\n Race Selection Menu")
                print("1. Human")
                print("2. Elf")
                print("3. Dragonborn")
                print("\n enter a number to select a race or type their name to see a descrition")
                racesel1=str(input())
                racesel2=racesel1.lower()
                if racesel2=="1":
                    racesel="Human"
                    break
                elif racesel2=="2":
                    racesel="Elf"
                    break
                elif racesel2=="3":
                    racesel="Dragonborn"
                    break
                elif racesel2=="human":
                    print("human desc")
                elif racesel2=="elf":
                    print("elf desc")
                elif racesel2=="dragonborn":
                    print("dragonborn desc")
                else:
                    print("Invalid Input")
        else:
            print("error")
else:
    print("bruh")