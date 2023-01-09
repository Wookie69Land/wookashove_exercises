import random

nums = list(range(1,50))
random.shuffle(nums)
lotto_nums = nums[:6]

rounds = 0
player_nums = []
while rounds < 6:
    try:
        x = int(input(f"Your {rounds+1} number: "))
        if x in range(1, 50) and x not in player_nums:
            player_nums.append(x)
            rounds += 1
        elif x in player_nums:
            print("Number already on the list!")
        elif x not in range(1, 50):
            print("Number out of range!")
    except ValueError:
        print("Not a number!")

player_nums = sorted(player_nums)
print(f"Player numbers: {player_nums}")

lotto_nums = sorted(lotto_nums)
print(f"Lotto numbers: {lotto_nums}")

guesses = []

for i in player_nums:
    if i in lotto_nums:
        guesses.append(i)
hit = len(guesses)
print(f"You got {hit} hits!")