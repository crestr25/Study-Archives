import pytest

from pathlib import Path # Standard way to represent the system paths
from tempfile import TemporaryDirectory
import cards

@pytest.fixture(scope="module") # module, because with session it fails
def cards_db():
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir) # Returns a Path object with the temp string
        db = cards.CardsDB(db_path) # instantiate a cardsdb.

        yield db

        db.close() # close connection (Bothersome)
