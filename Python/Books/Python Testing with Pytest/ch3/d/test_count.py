import cards

def test_empty(db):
    assert db.count() == 0


def test_two(db):
    db.add_card(cards.Card('first'))
    db.add_card(cards.Card('second'))

    assert db.count() == 2
