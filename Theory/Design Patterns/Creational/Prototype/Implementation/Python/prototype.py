import copy

class MyObject:
    """
    Python Prototype Pattern

    Python already implements its own interface of the pattern by the use of the library `copy`

        - copy.copy -> Shallow copy
        - copy.deepcopy -> deep copy 

    In order to implement it we must override the following methods.
        - __copy__
        - __deepcopy__ 
    """
    def __init__(self, mutable_obj, inmutable_obj):
        self.mutable_obj = mutable_obj
        self.inmutable_obj = inmutable_obj

    def __str__(self):
        return f"{self.__class__.__name__}(mutable_obj={self.mutable_obj}, inmutable_obj={self.inmutable_obj})"

    def __copy__(self):
        """
        Shallow copy.

        This method gets called whenever a call is made to copy.copy

        It should return a shallow copy of the object.
        """
        
        mutable_obj_copy = copy.copy(self.mutable_obj)
        new = self.__class__(mutable_obj_copy, self.inmutable_obj)
        print(new.__dict__)
        new.__dict__.update(self.__dict__)
        print(new.__dict__)

        return new

    def __deepcopy__(self, memo=None):
        """
        Deepcopy.

        What is the use of the argument `memo`? Memo is the dictionary that is
            used by the `deepcopy` library to prevent infinite recursive copies in
            instances of circular references. Pass it to all the `deepcopy` calls
            you make in the `__deepcopy__` implementation to prevent infinite
            recursions.
        """
        if memo is None:
            memo = {}

        mutable_obj_copy = copy.deepcopy(self.mutable_obj, memo)
        new = self.__class__(mutable_obj_copy, self.inmutable_obj)

        print(new.__dict__)
        new.__dict__ = copy.deepcopy(self.__dict__, memo)

        print(new.__dict__)

        return new

if __name__ == "__main__":
    list_obj = [1, [2, 3], {4, 5}]
    object_1 = MyObject(mutable_obj=list_obj, inmutable_obj=69)
    object_1_copy = copy.copy(object_1)

    print(object_1)
    print(object_1_copy)
    object_1_copy.mutable_obj.append(5)
    object_1_copy.mutable_obj[1].append(10)
    print(object_1)
    print(object_1_copy)


    list_obj_2 = [1, [2, 3], {4, 5}]
    object_2 = MyObject(mutable_obj=list_obj_2, inmutable_obj=69)
    object_2_copy = copy.deepcopy(object_2)

    print(object_2)
    print(object_2_copy)
    object_2_copy.mutable_obj.append(5)
    object_2_copy.mutable_obj[1].append(10)
    print(object_2)
    print(object_2_copy)