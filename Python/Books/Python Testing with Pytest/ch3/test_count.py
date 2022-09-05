import pytest

from pathlib import Path # Standard way to represent the system paths
from tempfile import TemporaryDirectory
import cards

@pytest.fixture()
def cardsdb():
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir) # Returns a Path object with the temp string
        db = cards.CardsDB(db_path) # instantiate a cardsdb.

        yield db

        db.close() # close connection (Bothersome)

def test_empty(cardsdb):
    assert cardsdb.count() == 0

def test_two(cardsdb):
    cardsdb.add_card(cards.Card('first'))
    cardsdb.add_card(cards.Card('second'))
    assert cardsdb.count() == 2
