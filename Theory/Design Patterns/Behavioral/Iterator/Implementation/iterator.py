from collections.abc import Iterable, Iterator
from typing import Any, List

"""
There are two abstract classes in python

1. the iterable class, which implements the __iter__() method (The collection)
2. the iterator class, which implements the __next__() method (The iterator)
"""

class AlphabeticalOrderIterator(Iterator):
    """
    This is the concrete class for the iterator which will
        - Implement the algorithm to traverse the collection
        - Store the current traversal position at all times
    """

    # First we need a _position attribute to store the actual position.
    # This can be extended to have multiple fields if the collection needs it
    _position: int = None

    # Indicate the traversal direction
    _reverse: bool = False

    def __init__(self, collection, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        """
        To implement the iterator the next method should return
            - The next item in the sequence.
            - Raise StopIteration exception
        """
        try:
            value = self._collection[self._position]
            self._position += 1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value

class WordsCollection(Iterable):
    """
    This is the Concrete collection implementation, it should
        - return the iterator object that is compatible with the collection
    """
    def __init__(self, collection: List[Any] = []) -> None:
        self._collection = collection

    def __iter__(self) -> AlphabeticalOrderIterator:
        """
        The iter method returns the iterator object.
        """
        return AlphabeticalOrderIterator(self._collection)

    def add_item(self, item: Any):
        self._collection.append(item)

if __name__ == "__main__":
    """
    The client code will work with the collection
    """

    collection = WordsCollection()
    collection.add_item("A")
    collection.add_item("B")
    collection.add_item("C")

    print("".join(i for i in collection))

    # it = iter(collection)

    # for i in range(10):
    #     print(next(it))


