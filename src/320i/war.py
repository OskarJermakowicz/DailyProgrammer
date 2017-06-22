import unittest

def play_war(player1, player2):
    deck_p1 = [int(s) for s in player1.split()]
    deck_p2 = [int(s) for s in player2.split()]

    while len(deck_p1) > 0 and len(deck_p2) > 0:
        card_p1 = deck_p1.pop(0)
        card_p2 = deck_p2.pop(0)

        if card_p1 > card_p2:
            deck_p1.insert(len(deck_p1), card_p1)
            deck_p1.insert(len(deck_p1), card_p2)
        elif card_p1 < card_p2:
            deck_p2.insert(len(deck_p2), card_p1)
            deck_p2.insert(len(deck_p2), card_p2)
        else:
            war_result = war(deck_p1, deck_p2)
            if war_result == 1:
                deck_p1.insert(len(deck_p1), card_p1)
                deck_p1.insert(len(deck_p1), card_p2)
            elif war_result == 2:
                deck_p2.insert(len(deck_p2), card_p1)
                deck_p2.insert(len(deck_p2), card_p2)

    if len(deck_p1) == 0 and len(deck_p2) == 0:
        return 0
    elif len(deck_p1) == 0:
        return 1
    elif len(deck_p2) == 0:
        return 2

def war(deck_p1, deck_p2):
    if len(deck_p1) == 0 and len(deck_p2) == 0:
        return 0
    elif len(deck_p2) == 0:
        return 1
    elif len(deck_p1) == 0:
        return 2

    cards_p1 = []
    cards_p2 = []

    if len(deck_p1) < 4 or len(deck_p2) < 4:
        cards_p1.extend(deck_p1[:min(len(deck_p1), len(deck_p2)) - 1])
        cards_p2.extend(deck_p2[:min(len(deck_p1), len(deck_p2)) - 1])
        del deck_p1[:min(len(deck_p1), len(deck_p2)) - 1]
        del deck_p2[:min(len(deck_p1), len(deck_p2)) - 1]
    else:
        cards_p1.extend(deck_p1[:3])
        cards_p2.extend(deck_p2[:3])
        del deck_p1[:3]
        del deck_p2[:3]

    card_p1 = deck_p1.pop(0)
    card_p2 = deck_p2.pop(0)

    if card_p1 > card_p2:
        deck_p1.extend(cards_p1)
        deck_p1.insert(len(deck_p1), card_p1)
        deck_p1.extend(cards_p2)
        deck_p1.insert(len(deck_p1), card_p2)
        return 1
    elif card_p2 > card_p1:
        deck_p2.extend(cards_p2)
        deck_p2.insert(len(deck_p2), card_p2)
        deck_p2.extend(cards_p1)
        deck_p2.insert(len(deck_p2), card_p1)
        return 2
    else:
        war_result = war(deck_p1, deck_p2)
        if war_result == 0:
            return 0
        elif war_result == 1:
            deck_p1.extend(cards_p1)
            deck_p1.insert(len(deck_p1), card_p1)
            deck_p1.extend(cards_p2)
            deck_p1.insert(len(deck_p1), card_p2)
            return 1
        elif war_result == 2:
            deck_p2.extend(cards_p2)
            deck_p2.insert(len(deck_p2), card_p2)
            deck_p2.extend(cards_p1)
            deck_p2.insert(len(deck_p2), card_p1)
            return 2

class test_war(unittest.TestCase):
    def test_player1_wins(self):
        self.assertEqual(play_war("5 1 13 10 11 3 2 10 4 12 5 11 10 5 7 6 6 11 9 6 3 13 6 1 8 1", "9 12 8 3 11 10 1 4 2 4 7 9 13 8 2 13 7 4 2 8 9 12 3 12 7 5"), 1)

    def test_player2_wins(self):
        self.assertEqual(play_war("3 11 6 12 2 13 5 7 10 3 10 4 12 11 1 13 12 2 1 7 10 6 12 5 8 1", "9 10 7 9 5 2 6 1 11 11 7 9 3 4 8 3 4 8 8 4 6 9 13 2 13 5"), 2)

    def test_draw(self):
        self.assertEqual(play_war("1 2 3 4 5 6 7 8 9 10 11 12 13 1 2 3 4 5 6 7 8 9 10 11 12 13", "1 2 3 4 5 6 7 8 9 10 11 12 13 1 2 3 4 5 6 7 8 9 10 11 12 13"), 0)

if __name__ == '__main__':
    unittest.main()