class Comet:
    def __init__(self, start, step, length, color, pixels):
        self.current = start
        self.step = step
        self.pixels = pixels
        self.colors = [
            tuple((c - ((i / (length - 1)) * c)) for c in color) for i in range(length)
        ] + [(0, 0, 0)]

    def __iter__(self):
        return self

    def __next__(self):
        self.current = (self.current + self.step) % len(self.pixels)
        for idx, item in enumerate(self.colors):
            self.pixels[(self.current + idx) % len(self.pixels)] = item
