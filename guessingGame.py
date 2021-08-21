import random 
rand=random.randint(1,9)
chances=0
while (chances<5):
    guess=int(input("guess a number!"))
    if(guess==rand):
        print("congratulations that's corrects!")
        break 
    elif(guess<rand):
        print("guess a higher number")
    else:
        print("guess a lower number")

    chances+=1

if not chances<5:
    print("you loose the number is", rand)