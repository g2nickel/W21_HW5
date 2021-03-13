import hw5_cards_ec2

c1 = hw5_cards_ec2.Card(1,1)
c2 = hw5_cards_ec2.Card(2,2)

print(c1)
print(c2)

h1 = hw5_cards_ec2.Hand([c1,c2])

d1 = hw5_cards_ec2.Deck()

hands = d1.deal(5,12)
print(len(d1.cards))
for x in hands:
    print("HanD!")
    for card in x.cards:
        print(card)