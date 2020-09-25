import time
import random
import os

CharacterInfo=[]
char=""
c=0

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
        print("1. race")
        print("2. class")

else:
    print("bruh")