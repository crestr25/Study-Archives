from pathlib import Path # Standard way to represent the system paths
from tempfile import TemporaryDirectory
import cards

def test_empty():
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir) # Returns a Path object with the temp string
        db = cards.CardsDB(db_path) # instantiate a cardsdb.

        count = db.count() # Count
        db.close() # close connection (Bothersome)

        assert count == 0
