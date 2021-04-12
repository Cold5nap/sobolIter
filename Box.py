class Box:
    def __init__(self, a, b, c):
        self.width, self.height, self.depth = sorted([a, b, c])

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getDepth(self):
        return self.depth

    def __str__(self):
        return "{"+str(self.width)+", "+ str(self.height)+", "+ str(self.depth)+"}"

    def __repr__(self):
        return str(self)

    def checkBoxPair(self, box):
        if self.depth > box.depth and self.width > box.width and self.height > box.height:
            return True
        return False
