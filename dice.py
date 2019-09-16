#Write a program named dice.py

#simulate 10000 plays of this came to determine which Player has an
#   advantage.

#Here’s what the program should involve:

from random import choices       #a. Import choices function from random module
ntrials=10000  #b. Set variable ntrials to 10000
nrolls=10000
total=0    #will keep track of all rolls done
tot=0
player1wins=0     #c. Set variable player1wins to 0
ndicep1=3  #number of dice rolled for player one
ndicep2=2  #number of dice rolled for player two
for i in range(ntrials):
        #d. Start loop over ntrials
        #setting a variable called dice thats equal to a list, rolling a six sided dice,
        #so (1,7) so it goes 1-6, number of dice rolled is given by k=ndice
        #e. Use choices() function to roll two dice for Player 2
    dicep2=choices(range(1,7),k=ndicep2) #will return list of ranndom dice rolls and store it in the list dice
        #f. Test if Player 2’s two dice are equal. If so, use continue to
        #  jump to the next trial in the loop
        #g. Use choices() function to roll three dice for Player 1
        #h. Sort the dice rolled by Player 1 using the .sort(reverse=True) function
    dicep2.sort(reverse=True)
        #i. Compare the sum of Player 1’s two highest dice to the sum of
        # Player 2’s two dice.
    dicep1=choices(range(1,7),k=ndicep1)
    dicep1.sort(reverse=True)
    total=total+dicep2[0]+dicep2[1]
    tot=tot+dicep1[0]+dicep1[1]+dicep1[2]
    if tot>total :
        player1wins=player1wins+1  #If Player 1’s sum is greater than Player 2’s then add 1 to player1wins
    #else:
       # print("average roll for player two was greater than player one")
print("Player two is rolling two dice ten-thousand times.")
print("Player one is rolling three dice ten-thousand times.")
print("Average roll for player two is =", total/ntrials)
print("Average roll for player one is =", tot/nrolls)
print("Player one won a total of", player1wins, "games.")
print("The ratio of player one's wins to total games is", player1wins/ntrials)   #j. Outside of the loop, print out the ratio of player1wins to ntrials
#Thought questions: How fair is this game? That is, how close to 50% is Player 1’s winning probability
