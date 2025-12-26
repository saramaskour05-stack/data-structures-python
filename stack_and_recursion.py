class Array:
    def __init__(self, size, data_type, value=None):
        self.size = size
        self.type = data_type
        self.items = [value] * size

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, new):
        if type(new) == self.type:
            self.items[index] = new


class StackArray:
    def __init__(self, size, data_type):
        self.stack = Array(size, data_type)
        self.top = -1
        self.size = size

    def push(self, value):
        if self.top == self.size - 1:
            return "Stack overflow"
        self.top += 1
        self.stack[self.top] = value

    def pop(self):
        if self.top == -1:
            return None
        value = self.stack[self.top]
        self.top -= 1
        return value
