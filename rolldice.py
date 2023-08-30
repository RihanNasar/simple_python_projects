import random

def roll():
    min_val = 1
    max_val = 6
    roll = random.randint(min_val,max_val)

    return roll
while True:
    players = input(" enter the number of players")
    if(players.isdigit()):
        players = int(players)
        if 2<=players<=5:
            break
        else:
            print("players must be between 1-5 ")
    else: 
        print("invalid try again")
max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:

    for i in range(players):
        print("\n player number", i +1 ,"has just started")
        current_score = 0
        while True:
            should_roll = input("would you like to roll (y)")
            if (should_roll.lower()) != "y":
                break;
            value = roll()
            if value == 1:
                print("you roled a one , turn done")
                current_score = 0
                break
            else:
                current_score +=1
                print("you rolled a ",value)
        player_scores[i] += current_score
        print("your total score is ", player_scores[i])
max_score = max(player_scores)
winning_idx = player_scorers.index(max_score)
print("player number ", winning_index+1,"has won with a score of ",max_score)

