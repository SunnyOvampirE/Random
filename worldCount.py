text=input("Please enter your text")


cars=0
words=1

for i in text:
    cars=cars+1
    if i == " ":
        words=words+1

print ("you have "+ str(cars)+" characters")
print ("you have",words,"words" )