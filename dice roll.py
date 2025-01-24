import random
name1=str(input("Enter player 1's name"))
name2=str(input("Enter player2's name"))

def dice():
     a = random.randint(1,6)
     return a

dice()

total_score1 = 0
total_score2 = 0

while a in range (5):
     score = dice() + dice()
     if score % 2 == 0:
          total_score = score + 10
     else:
          total_score = score - 5
     input()
     print(name1, "score at the end of 5 rounds is", total_score)
     break

while a in range (5):
     score = dice() + dice()
     if score % 2 == 0:
          total_score = score + 10
     else:
          total_score = score - 5
     input()
     print(name2, "score at the end of 5 rounds is", total_score)
     break