from enum import Enum


class Suit(Enum):
    Clubs = 1
    Diamonds = 2
    Hearts = 3
    Spades = 4


SUIT_LETTER_TO_SUIT = {
    "C": Suit.Clubs,
    "D": Suit.Diamonds,
    "H": Suit.Hearts,
    "S": Suit.Spades,
}

FACE_VALUES = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]


class Card:
    """
    A card from a standard deck, ignoring wildcards. Has a value and suit.
    Value: 2-10, J, Q, K, A
    Suit: Clubs, Diamonds, Hearts, Spades
    """

    def __init__(self, card_string):
        """
        :param card_string: String representing a card, consisting of face
        and suit concatenated. e.g. 9H (9 of hearts) of AC (ace of clubs.)
        """
        card_string = card_string.upper()
        self.suit = SUIT_LETTER_TO_SUIT.get(card_string[-1])
        if self.suit is None:
            raise ValueError("Suit not recognised or incorrect card string format used")
        self.face = card_string[:-1]
        if self.face not in FACE_VALUES:
            raise ValueError(
                "Face value not recognised of incorrect card string format used"
            )
