import pytest

from pokerpy.Card import Card, Suit


@pytest.mark.parametrize(
    "card_string,face,suit",
    [
        ("2C", "2", Suit.Clubs),
        ("10D", "10", Suit.Diamonds),
        ("JH", "J", Suit.Hearts),
        ("QS", "Q", Suit.Spades),
        ("KS", "K", Suit.Spades),
        ("AH", "A", Suit.Hearts),
    ],
)
def test_create_real_card(card_string, face, suit):
    card = Card(card_string)
    assert card.face == face
    assert card.suit == suit


@pytest.mark.parametrize("card_string", ["1C", "11S", "2B", "77", "AA"])
def test_create_fake_card(card_string):
    with pytest.raises(ValueError):
        Card(card_string)


@pytest.mark.parametrize("card_string", ["C2", "DJ"])
def test_wrong_card_syntax(card_string):
    with pytest.raises(ValueError):
        Card(card_string)


def test_repr():
    """
    Test that repr gives a vaguely useful response rather than an object id.
    """
    card = Card("8C")
    assert "8" in repr(card)
    assert "C" in repr(card) or "clubs" in card.lower()


def test_str():
    """
    Test that str gives a vaguely useful response rather than an object id.
    """
    card = Card("8C")
    assert "8" in repr(card)
    assert "C" in repr(card) or "clubs" in card.lower()


def test_comparison_equals():
    """
    Test equality comparison.
    """
    a = Card("3H")
    b = Card("8C")
    c = Card("3H")
    assert a == c
    assert c == a
    assert a == a
    assert b == b
    assert c == c
    assert a != b and b != a and c != b and b != c


def test_value_comparison_equals():
    a = Card("QC")
    b = Card("QD")
    c = Card("QH")
    d = Card("QS")
    assert a.value == b.value == c.value == d.value


def test_value_comparison_numbers():
    for i in range(2, 10):
        a = Card(f"{i}H")
        b = Card(f"{i + 1}H")
        assert a.value < b.value


def test_value_comparison_complex():
    assert Card("10H").value < Card("JC").value
    assert Card("JC").value < Card("QS").value
    assert Card("QS").value < Card("KD").value
    assert Card("KD").value < Card("AH").value
    assert Card("2C").value < Card("AH").value
