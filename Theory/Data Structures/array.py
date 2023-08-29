class Array:
    def __init__(self) -> None:
        self.length = 0
        self.data = []

    def get(self, index):
        try:
            rv = self.data[index]
        except:
            raise IndexError

        return rv

    def push(self, item):
        self.data.append(item)
        self.length += 1

    def pop(self):
        rv = self.data.pop()
        self.length -= 1
        return rv

    def delete(self, index):
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]

        self.data.pop()
        self.length -= 1

    def __repr__(self) -> str:
        return f"{self.data} of length: {self.length}"


if __name__ == "__main__":
    myArr = Array()
    myArr.push(1)
    myArr.push(2)
    myArr.push(3)
    myArr.get(0)
    myArr.delete(1)
    print(myArr)
