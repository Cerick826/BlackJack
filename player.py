""" This is the player.py file """


from cards import Deck


class Player:
    def __init__(self, name, deck):
        """This is the __init__ funct"""

        self._name = name
        self._deck = deck
        self._hand = []
        self._card = []
        self._score = 0
        self._bet = 0
        self._ace = False
        self._dScore = 0
        self._blackJack = False
        self._win = True
        self._matching = False
        self._splitHand = []

    @property
    def name(self):
        """This is the name funct"""
        return self._name

    @property
    def score(self):
        """This is the score funct"""
        return self._score

    def hit(self):
        # TODO:
        """This is the hit funct"""
        pass

    def deal_Hand(self):
        self._card = self._deck.deal(1)
        self._hand.extend(self._card)
        self.check_Score(-1)

        print(self._hand[-1], ",", end=" ")

        self._card = self._deck.deal(1)
        self._hand.extend(self._card)
        self.check_Score(-1)

        print(self._hand[-1])
        print("Total is: ", self._score)

        if self._score == 21:
            return 1

        elif self._hand[0] == self._hand[1]:
            self._matching = True
            return 0

        return 0

    def split(self):
        """This is the split funct"""
        # TODO
        pass

    def double_down(self):
        # TODO
        pass

    def check_Score(self, index):
        """This is the check_Score funct"""

        if (
            self._hand[index].rank == "King"
            or self._hand[index].rank == "Queen"
            or self._hand[index].rank == "Jack"
        ):
            score = 10

        elif self._hand[index].rank == "Ace":
            score = 11
            self._ace = True

        elif int(self._hand[index].rank) in range(1, 11):
            score = int(self._hand[index].rank)

        self._score += score

    def am_i_dealer(cls):
        """This is the am_i_dealer funct"""
        return False

    def check_shoe(self):
        """Check to see if the dealer has reached the cut\
            card, if so re-prepare the shoe."""
        if len(self._deck <= 208):
            for _ in range(4):
                self._deck.merge(Deck())
            Deck.shuffle(self._deck, 20)
            Deck.cut(self._deck)


class Dealer(Player):
    def __init__(self, name, deck):
        super().__init__("Dealer", deck)

    def am_i_dealer(cls):
        """This is the am_i_dealer funct"""
        return True

    def hit(self):
        """This is the hit funct"""
        # TODO
        pass

    def deal_Hand(self):
        self._card = self._deck.deal(1)
        self._hand.extend(self._card)
        self.check_Score(-1)

        print(self._hand[-1], ", ?")
        print("Total is: ", self._dScore)

        self._card = self._deck.deal(1)
        self._hand.extend(self._card)
        self.check_Score(-1)

        if self._score == 21:
            return 1

        return 0

    def show_cards(self):
        print("--------------------------------------------")
        print(self._name + "'s cards")
        for i in range(0, len(self._hand)):
            print(self._hand[i], ",", end=" ")

        print("\n")
        print("Total is: ", self._score)
        # print("--------------------------------------------")

        if self._score >= 17:
            return 1
        return 0

    def check_Score(self, index):
        """This is the check_Score funct"""
        # self._score = card_value(self._card)
        # print(self._hand[index].rank)

        if (
            self._hand[index].rank == "King"
            or self._hand[index].rank == "Queen"
            or self._hand[index].rank == "Jack"
        ):
            score = 10

        elif self._hand[index].rank == "Ace":
            if self._ace == True:
                score = 1

            else:
                score = 11
                self._ace = True

        elif int(self._hand[index].rank) in range(1, 11):
            score = int(self._hand[index].rank)

        self._dScore = score
        self._score += score

    def deal_to(self, player):
        pass

    def check_shoe(self):
        """Check to see if the dealer has reached the cut\
            card, if so re-prepare the shoe."""
        pass
