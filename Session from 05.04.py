import random


class Card:
    SUITS = ["♣", "♦", "♥", "♠"]
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def _init_(self, rank, suit):
        if rank not in self.RANKS:
            raise Exception(f"Invalid rank, must be one of {self.RANKS}")
        if suit not in self.SUITS:
            raise Exception(f"Invalid suit, must be one of {self.SUITS}")
        self._rank = rank
        self._suit = suit

    @property
    def suit(self):
        return self._suit

    @property
    def rank(self):
        return self._rank

    def _str_(self):
        return f"{self.rank}{self.suit}"

    def _repr_(self):
        return self._str_()


class Deck:
    def _init_(self):
        cards = []
        # iterate over all ranks and suits, create a card and add it to the list
        for rank in Card.RANKS:
            for suit in Card.SUITS:
                card = Card(rank, suit)
                cards.append(card)
        self._cards = tuple(cards)

    @property
    def cards(self):
        return self._cards

    def _str_(self):
        return str(self.cards)

    def shuffle(self):
        # shuffles the cards in the deck
        cards = list(self.cards)
        random.shuffle(cards)
        self._cards = tuple(cards)


class Hand:
    def _init_(self, deck):
        # deck is shuffled before
        cards = []
        for i in range(5):
            cards.append(deck.cards[i])
        self._cards = tuple(cards)

    def _str_(self):
        return str(self._cards)

    @property
    def cards(self):
        return self._cards

    @property
    def is_flush(self):
        suit = self._cards[0].suit
        for i in range(1, 5):
            if self._cards[i].suit != suit:
                return False

        return True

    @property
    def is_pair(self):
        ranks = []
        for card in self.cards:
            ranks.append(card.rank)
        for rank in ranks:
            if ranks.count(rank) == 2:
                return True
        return False


precision = tries = 10
i = 0
while True:
    i = i + 1
    d = Deck()
    d.shuffle()
    hand = Hand(d)
    if hand.is_pair:
        tries -= 1

    if tries == 0:
        break

probability = precision / i * 100
print(f"The odds of getting a pair are {probability}%")


@property
def is_full_house(self):
    return self. is .3
    _kind and self.is_pair

    @property
    def is_2_pair(self):
        ranks = []
        for card in self.cards:
            ranks.append(card.rank)
        ranks = set(ranks)
        if len(ranks) == 3 and not self.is_3_kind
            return True
        return False


precision = tries = 10
i = 0
while True:
    i = i + 1
    d = Deck()
    d.shuffle()
    hand = Hand(d)
    is hand.is_full_house:
    tries -= 1

if tries == 0:
    break