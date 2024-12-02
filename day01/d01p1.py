#references

def main():

    left, right = [], []

    with open("day01/input.txt") as file:
        for line in file:
            line = line.split()
            left.append(int(line[0]))
            right.append(int(line[1]))
    
    left.sort()
    right.sort()

    sum = 0
    for l, r in zip(left, right):
        sum += abs(l-r)
    
    print(sum)

main()