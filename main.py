from Box import Box
from sys import argv
from Iteration import BoxIteration


def calculate(boxes):
    iterator = iter(BoxIteration(boxes))
    inners = []
    #index нужен для inners
    for i in range(len(boxes)):
            inners.append([])
            print()
            for compareBox in BoxIteration(boxes):
                if compareBox != boxes[i] and boxes[i].checkBoxPair(compareBox):
                    inners[i].append(compareBox)
                    print(compareBox)

    return inners


def read_in_file(path):
    f = open(path)
    listOfBoxes = []
    for line in f:
        chars = line.split(" ")
        listOfBoxes.append(Box(int(chars[0]), int(chars[1]), int(chars[2])))
    return listOfBoxes


def main():
    if len(argv) > 1:
        path = argv[1]
    else:
        path = input("Enter file name: ")
    calculate(read_in_file(path))
# print(r)


if __name__ == '__main__':
    main()
