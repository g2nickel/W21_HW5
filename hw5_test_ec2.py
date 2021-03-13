###########################################
##### NAME: Greg Nickel          ##########
##### Uniqname: gnickel          ##########
###########################################

import unittest
import hw5_cards_ec2

class TestPart2(unittest.TestCase):

    def testPairs(self):
        """Give a variety of 5-card hands, check the number of cards in each hand
         after pairs are removed
         """
        c1 = hw5_cards_ec2.Card(0,4)
        c2 = hw5_cards_ec2.Card(1,4)
        c3 = hw5_cards_ec2.Card(2,4)
        c4 = hw5_cards_ec2.Card(3,4)
        c5 = hw5_cards_ec2.Card(0,5)
        c6 = hw5_cards_ec2.Card(1,5)
        c7 = hw5_cards_ec2.Card(3,6)
        c8 = hw5_cards_ec2.Card(2,7)
        c9 = hw5_cards_ec2.Card(3,8)
        two_pair = [c1,c2,c7,c6,c5]
        full_house = [c1,c2,c3,c6,c5] #Check if there is three of a kind
        no_pair = [c1,c5,c7,c8,c9]
        four_of_a_kind = [c1,c2,c3,c4,c5]
        h1 = hw5_cards_ec2.Hand(two_pair)
        h2 = hw5_cards_ec2.Hand(full_house)
        h3 = hw5_cards_ec2.Hand(no_pair)
        h4 = hw5_cards_ec2.Hand(four_of_a_kind)
        h1.remove_pairs()
        h2.remove_pairs()
        h3.remove_pairs()
        h4.remove_pairs()
        self.assertEqual(len(h1.cards),1)
        self.assertEqual(len(h2.cards),1)
        self.assertEqual(len(h3.cards),5)
        self.assertEqual(len(h4.cards),1)

    def testDeal(self):
        number_of_hands = [4,5,7,10,50]
        size_of_hands = [7,4,-1,-1,2]
        for x in range(4):
            d1 = hw5_cards_ec2.Deck()
            hands = d1.deal(number_of_hands[x],size_of_hands[x])
            card_total = len(d1.cards)
            for hand in hands:
                card_total += len(hand.cards)
            self.assertEqual(card_total,52)
            #The total cards dealt up, plus remaining in deck =52

if __name__=="__main__":
    unittest.main()
