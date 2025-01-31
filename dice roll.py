import random
name1=str(input("Enter player 1's name"))
name2=str(input("Enter player2's name"))
def roll_dice():
    """Simulate rolling two 6-sided dice."""
    return random.randint(1, 6), random.randint(1, 6)

def calculate_score(total):
    """Calculate the score based on the total of the two dice rolls."""
    if total % 2 == 0:
        return total + 10  # If even, add 10 points
    else:
        return max(0, total - 5)  # If odd, subtract 5 points, ensure score doesn't go below 0

def play_round(player):
    """Simulate a round for a single player, rolling two dice."""
    die1, die2 = roll_dice()
    total = die1 + die2
    score = calculate_score(total)
    print(f"{player} rolled {die1} and {die2}, total: {total}, score for this round: {score}")
    return score
    input()

def main():
    # Initialize scores
    player1_score = 0
    player2_score = 0

    # Play 5 rounds
    for round_num in range(1, 6):
        print(f"\nRound {round_num}:")

        # Player 1's turn
        player1_score += play_round(name1)
        print(f"", name1, " total score:",player1_score)

        # Player 2's turn
        player2_score += play_round(name2)
        print(f"", name2," total score:",player2_score)

    # Check if there's a tie after 5 rounds
    if player1_score > player2_score:
        print("\n",name1," wins!")
    elif player2_score > player1_score:
        print("\n",name2, " wins!")
    else:
        print("\nIt's a tie after 5 rounds. Time for a tiebreaker!")

        # Tiebreaker: each player rolls 1 die until someone wins
        while player1_score == player2_score:
            print("\nTiebreaker round:")
            player1_roll = random.randint(1, 6)
            player2_roll = random.randint(1, 6)

            print(f"",name1, "rolled:",player1_roll)
            print(f"",name2,"rolled:",player2_score)

            if player1_roll > player2_roll:
                print("\n",name1," wins the tiebreaker!")
                break
            elif player2_roll > player1_roll:
                print("\n",name2," wins the tiebreaker!")
                break
            else:
                print("\nIt's a tie in the tiebreaker, rolling again!")

if __name__ == "__main__":
    main()

