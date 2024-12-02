#references

def main():

    left, right = [], []

    with open("day01/input.txt") as file:
        for line in file:
            line = line.split()
            left.append(int(line[0]))
            right.append(int(line[1]))

    sum = 0
    for l in left:
        sum += l * right.count(l)
    
    print(sum)

main()