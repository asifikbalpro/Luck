

from random import randrange
import numpy as np

# getting the percentage down to 100
def percentage(down):
    return ((randrange(1, 101)* down)/100) # eq

# genarating data
def luck():
    participants = 100000
    skill = []
    luck = []
    for i in range(participants):
        s = percentage(95)
        skill.append(s)
        l = percentage(5)
        luck.append(l)
        # print(skill[i], " ", luck[i])
        
    total_score = []
    for i in range(participants):
        total_score.append(skill[i]+luck[i])
        print(total_score[i])

    
    

    total_score.sort(reverse=True)

    for i in range(50):
        print("Highest score: ", total_score[i])

def main():
    print("Hello World!")
    luck()

if __name__ == "__main__":
    main()

