
# no of guesses 9
# print no of guesses left
# No of guesses he took to finish
# game over

n=18
g=1
print("You can guess only 9 times")
while(g<=9):
    print("Guess the no")
    inp=int(input())
    if inp<18:
        print("You have entered lesser no please increase the no")
    elif inp>18:
        print("You have entered greater no please decrease the no")
    else:
        print("You won")
        print(g,"no of guesses he took to finish")
        break
    print(9-g,"no of guesses left")
    g=g+1

    if g>9:
        print("Game over")



