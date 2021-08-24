class letter():
    def __init__(self, value, position):
        self.value = value
        self.position = position

    def __repr__(self):
        return self.value

def what_speaks_only_when_spoken_to():
    return [
        letter('c', 4),
        letter('a', 0),
        letter('e', 3),
        letter('o', 6),
        letter(' ', 2),
        letter('n', 1),
        letter('h', 5)
    ]

if __name__ == '__main__':
    print(what_speaks_only_when_spoken_to())
