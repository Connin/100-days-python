import random
import sys
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

user_cards = []
dealer_cards = []

def ace_handle(hands):
    while sum(hands) > 21 and 11 in hands:
        hands[hands.index(11)] = 1

def check21(hands):
    ace_handle(hands)
    return sum(hands) > 21

#user_cards = [random.choice(cards), random.choice(cards)]
user_cards = [11,11]
print(f"You have {user_cards}")
#dealer_cards = [random.choice(cards), random.choice(cards)]
dealer_cards = [11,11]

ace_handle(dealer_cards)

while sum(dealer_cards) < 17:
    dealer_cards.append(random.choice(cards))
    ace_handle(dealer_cards)
    

print(f"Dealer has {dealer_cards[0]} and X")

conti = input("proceed? Y or N").lower()
while conti == "y":
    user_cards.append(random.choice(cards))
    print(f"You have {user_cards}")
    check21(user_cards)
    conti = input("proceed? Y or N").lower()


print(f"Dealer has {dealer_cards}")

if check21(user_cards) == True:
    print("Busted. You lost")
    sys.exit()

if sum(user_cards) > sum(dealer_cards) or check21(dealer_cards) == True:
    print("u win")
    if check21(dealer_cards) == True:
        print("dealer busted")
elif sum(user_cards) < sum(dealer_cards):
    print("u lost")
else:
    print("Draw")

