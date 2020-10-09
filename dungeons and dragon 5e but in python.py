import time
import random
import os

CharacterInfo=[]
char=""
c=0
racesel="none"
classsel="none"
bckgsel="none"
name=""

print("checking for existing character in directory")
try:
    char=open("character.txt","r+")
    print("existing character found")
    c+=1
except:
    print("no character found, skipping to character creation\n")

if c==0:
    while True:
        print(" Character Creation Menu \n")
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
        elif sel=="2":
            while True:
                print("\n Class Selection Menu")
                print("1. Fighter")
                print("2. Wizard")
                print("3. Monk")
                print("\n enter a number to select a class or type its name to see a descrition")
                classsel1=str(input())
                classsel2=classsel1.lower()
                if classsel2=="1":
                    classsel="Fighter"
                    break
                elif classsel2=="2":
                    classsel="Wizard"
                    break
                elif classsel2=="3":
                    classsel="Monk"
                    break
                elif classsel2=="fighter":
                    print("fighter desc")
                elif classsel2=="wizard":
                    print("wizard desc")
                elif classsel2=="monk":
                    print("monk desc")
                else:
                    print("Invalid Input")
        elif sel=="3":
            while True:
                print("\n Background Selection Menu")
                print("1. Noble")
                print("2. Outlander")
                print("3. Sage")
                print("\n enter a number to select a background or type its name to see a descrition")
                bckgsel1=str(input())
                bckgsel2=bckgsel1.lower()
                if bckgsel2=="1":
                    bckgsel="Noble"
                    break
                elif bckgsel2=="2":
                    bckgsel="Outlander"
                    break
                elif bckgsel2=="3":
                    bckgsel="Sage"
                    break
                elif bckgsel2=="noble":
                    print("noble desc")
                elif bckgsel2=="outlander":
                    print("outlander desc")
                elif bckgsel2=="sage":
                    print("sage desc")
                else:
                    print("Invalid Input")
        elif sel=="":
            if racesel!="none" and classsel!="none" and bckgsel!="none":
                name=input("enter your character's name")
                print("creating character")
                char=open("character.txt","w")
                char.writelines([racesel,"\n",classsel,"\n",bckgsel,"\n",name])
                char.close()
                print("character saved")
                break
            else:
                print("missing selections!")
        else:
            print("error")
else:
    with open ("character.txt", "r") as char:
        data=char.read().splitlines()
    racesel=data[0]
    classsel=data[1]
    bckgsel=data[2]
    name=data[3]
    #print(racesel)
    #print(classsel)
    #print(bckgsel)
    #print(name)
print("You sit around a sturdy wooden table lit by a brightly burning candle and littered with plates cleared of food and half-drained tankards.")
print("The sounds of gamblers yell-ing and d runken adventurers singing bawdy songs nearly drown out the off-key strumming of a young bard three tables over.")
print("Then all the noise is eclipsed by a shout: 'Ya pig! Like killin' me mates, does ya?' Then a seven-foot-tall half-orc is hit by a wild,")
print("swinging punch from a male human whose shaved head is covered with eye-shaped tattoos. Four other humans stand behind him, ready to jump Into the fray.")
print("The half-ore cracks her knuckles, roars,  and leaps at the tattooed figure-but before you can see if blood is drawn, a crowd of spectators clusters around the brawl.")
print("What do you do?\n")
print("OPTIONS")
print("1. watch")
print("2. join the fight")
while True:
    wdyd=input()
    if wdyd=="1":
    
    elif wdyd=="2":
        print("you get up off your stool and join the fight...")
        print("\n-=COMBAT-=-START=-\n")
        print("particapants:")
        print()
    else:
        print("")

#TEXT FILE FORMAT
#name
#ally/enemy
#hp
#damage
