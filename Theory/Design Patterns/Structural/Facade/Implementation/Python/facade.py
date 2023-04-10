class Buffer:
    def __init__(self, width=30, height=20) -> None:
        self.width = width
        self.heigth = height
        self.buffer = [' '] * (width*height)
    
    def __getitem__(self, item):
        return self.buffer.__getitem__(item)

    def write(self, text):
        self.buffer += text


class Viewport:
    def __init__(self, buffer=None):
        if not buffer:
            buffer = Buffer()
        self.buffer = buffer
        self.offset = 0
    
    def get_char_at(self, index):
        self.buffer[index+self.offset]

    def append(self, text):
        self.buffer.write(text)