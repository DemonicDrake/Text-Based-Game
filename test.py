test="test"
try:
    temp=open("temp.txt","w+")
except:
    print("ohfuck")
temp.write(test)
