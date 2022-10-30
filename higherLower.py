from art import logo, vs
import random
from game_data import data

print(logo)


def generateRandom(num):
    return random.randint(0, num - 1)


isGameOn = True
score = 0
Turn = 5
numOfData = len(data)
num1 = generateRandom(numOfData)
while isGameOn and Turn > 0:
    num2 = generateRandom(numOfData)
    while num2 == num1:
        num2 = generateRandom(numOfData)
    followerCount1 = data[num1]['follower_count']
    followerCount2 = data[num2]['follower_count']
    #name1 =
    output1 = f"{data[num1]['name']}, a {data[num1]['description']}, from ${data[num1]['country']}."
    output2 = f"{data[num2]['name']}, a {data[num2]['description']}, from ${data[num2]['country']}."
    print(f"Compare A: {output1}")
    print(vs)
    print(f"compare B: {output2}")
    userInput = input("Who has more followers? Type 'A' or 'B': ")
    if (userInput == 'A' and followerCount1 >= followerCount2) or (
            userInput == 'B' and followerCount1 < followerCount2):
        score += 1
        print(f"You are right. Current score is {score}")
    else:
        print(f"OOps!! Incorrect answer. Current score is {score}")
    Turn -= 1
    num1 = num2

print(f"Your final score is {score}")
