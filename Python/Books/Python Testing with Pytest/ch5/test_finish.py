from cards import Card

def test_finish_from_in_prog(db):
    index = db.add_card(Card("second edition", state="in prog"))
    db.finish(index)
    card = db.get_card(index)
    assert card.state == 'done'

def test_finish_from_in_done(db):
    index = db.add_card(Card("second edition", state="done"))
    db.finish(index)
    card = db.get_card(index)
    assert card.state == 'done'

def test_finish_from_in_todo(db):
    index = db.add_card(Card("second edition", state="todo"))
    db.finish(index)
    card = db.get_card(index)
    assert card.state == 'done'
