from Box import Box
from sys import argv
from iter import Iteration


def calculate(data1):
    result = []
    iterator = iter(Iteration(data1))
    while True:
        try:
            c = next(iterator)
            if :
            else:

        except StopIteration:
            break

    # for i in range(len(data1)):
    #     for j in range(len(data1)):
    #         if data1[i].checkBoxPair(data1[j]):
    #             result.append((data1[i], data1[j]))

    return result


def ReadInFile(data):
    with open(data, "r") as txt_file:
        input_data = [Box(int(line.split()[2]), int(line.split()[1]), int(line.split()[0])) for line in txt_file]
    return input_data


def main():
    if len(argv) > 1:
        data = argv[1]
    else:
        data = input("Enter file name: ")
    r = calculate(ReadInFile(data))
    print(r)


if __name__ == '__main__':
    main()
