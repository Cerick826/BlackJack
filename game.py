""" This is the game.py file """


from cards import Deck
from player import Player, Dealer
from time import sleep


class BlackJackGame:
    def __init__(self):
        self._deck = Deck()
        self._player = []
        self._dealer = []
        self._game_is_not_over = True

    def run(self):

        """runs the game"""

        print("Welcome to BlackJack")

        # creates multiple decks
        for _ in range(7):
            self._deck.merge(Deck())

        # shuffles deck
        Deck.shuffle(self._deck, 20)
        Deck.cut(self._deck)

        # intialize the players
        num_players = int(input("How many players? [1-4] "))
        for i in range(1, num_players + 1):
            print("Player", i, "What is your name?", end=" ")
            name = input()
            self._player.append(Player(name, self._deck))

        current_player_index = 0

        # adds dealer to players
        self._player.append(Dealer(name, self._deck))

        # initialize the bets
        while self._game_is_not_over:
            """initialize the players"""
            current_player_index = 0
            cp = self._player[current_player_index]
            for i in range(1, num_players + 1):
                cp = self._player[current_player_index]
                print("--------------------------------------------")
                print("\n", cp._name, "is up!\n".format(cp))
                cp._bet = int(input("How much would you like to bet? "))
                current_player_index = (current_player_index + 1) % len(self._player)
                sleep(1)

            current_player_index = 0

            # deals and shows cards
            for i in range(1, len(self._player) + 1):
                cp = self._player[current_player_index]
                print("--------------------------------------------")
                print("\n" + cp._name + "'s cards")

                if cp.am_i_dealer() == False:
                    result = cp.deal_Hand()
                    # blackjack
                    if result == 1:
                        print("Congrats, you got a BlackJack!")
                        cp._blackJack = True
                    # next player
                    current_player_index = (current_player_index + 1) % len(
                        self._player
                    )

                else:
                    result = cp.deal_Hand()
                    current_player_index = (current_player_index + 1) % len(
                        self._player
                    )

            # resets back to first player
            current_player_index = 0
            for i in range(1, len(self._player) + 1):
                cp = self._player[current_player_index]
                looper = True

                # game loop
                while looper:
                    if cp.am_i_dealer() == False:
                        if cp._blackJack == False:

                            print("-------------------------------------------")
                            print(
                                "\n"
                                + cp._name
                                + " would you like to hit, stay, or double down?",
                                end=" ",
                            )
                            print("Current Score:", cp._score, "(H/S/D)", end=" ")

                            response = str(input())
                            response = response.lower()
                            print("\n")

                            if response == "h" or response == "hit":
                                result = cp.hit()
                                if result == 1:
                                    print("You Busted!")
                                    cp._win = False
                                    looper = False
                                    current_player_index = (
                                        current_player_index + 1
                                    ) % len(self._player)

                            else:
                                looper = False
                                current_player_index = (current_player_index + 1) % len(
                                    self._player
                                )
                        else:
                            looper = False
                            current_player_index = (current_player_index + 1) % len(
                                self._player
                            )
                    else:
                        looper = False
                        current_player_index = (current_player_index + 1) % len(
                            self._player
                        )

            # dealer portion
            loop = True
            while loop:
                sleep(1)
                result = cp.show_cards()
                if result == 0:
                    test = cp.hit()
                    if test == 1:
                        print("Dealer Busted!")
                        cp._win = False
                        loop = False

                else:
                    loop = False

            sleep(1)

            current_player_index = 0
            for i in range(1, num_players + 1):
                cp = self._player[current_player_index]
                print("--------------------------------------------")

                # TODO: Implement win conditions here

            print("--------------------------------------------")
            response = input("\nWould you like another hand (y/n) ")
            response = response.lower()
            if response == "y" or response == "yes":
                # print("--------------------------------------------")
                current_player_index = 0
                for i in range(1, len(self._player) + 1):
                    cp = self._player[current_player_index]
                    current_player_index = (current_player_index + 1) % len(
                        self._player
                    )
                self._game_is_not_over = True

            else:
                self._game_is_not_over = False

        print("Thanks for playing!")

        sleep(1)
