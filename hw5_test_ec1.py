###########################################
##### NAME: Greg Nickel          ##########
##### Uniqname: gnickel          ##########
###########################################

import unittest
import hw5_cards_ec1

class TestHand(unittest.TestCase):

    def test_init(self):
        c1 = hw5_cards_ec1.Card(1,2)
        c2 = hw5_cards_ec1.Card(2,4)
        h1 = hw5_cards_ec1.Hand([c1,c2])
        self.assertIsInstance(h1,hw5_cards_ec1.Hand)

    def testAddAndRemove(self):
        c1 = hw5_cards_ec1.Card(1,2)
        c2 = hw5_cards_ec1.Card(2,4)
        h2 = hw5_cards_ec1.Hand()
        n0 = len(h2.cards)
        h2.add_card(c1)
        n1 = len(h2.cards)
        h2.remove_card(c1)
        n2 = len(h2.cards)
        self.assertEqual(n0,n2)
        self.assertEqual(n1-1,n2)

    def testDraw(self):
        d1 = hw5_cards_ec1.Deck()
        h1 = hw5_cards_ec1.Hand()
        d1_start_length = len(d1.cards)
        h1_start_length = len(h1.cards)
        h1.draw(d1)
        d1_end_length = len(d1.cards)
        h1_end_length = len(h1.cards)
        start_cards = d1_start_length + h1_start_length
        end_cards = d1_end_length + h1_end_length
        self.assertEqual(start_cards,end_cards)
        self.assertEqual(d1_start_length,d1_end_length+1)
        self.assertEqual(h1_start_length,h1_end_length-1)

if __name__=="__main__":
    unittest.main()
