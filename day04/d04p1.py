#find the number of XMAS in each line, given a list of lines (just linearly, does not act like a board)
def findXMAS(lines):
    total = 0
    for line in lines:
        for i in range(len(line)-3):
            if line[i:i+4] == 'XMAS':
                total += 1
            if line[i:i+4] == 'SAMX':
                total += 1
    return total


def main():

    #definitely not the most elegant solution
    #4 lists, to represent the board in the 4 directions, 
    #  which are the four directions (with forwards and backwards each direction) you can form a valid word
    horizontal, vertical, diagonal1, diagonal2 = [], [], [], []

    with open("day04/input.txt") as file:

        line = file.readline().rstrip()
        horizontal.append(line)
        for l in line:
            vertical.append(l)
            diagonal1.append(l)
            diagonal2.append(l)
        
        j = 0
        for line in file:
            line = line.rstrip()
            horizontal.append(line)

            vertical[0] += line[0]
            diagonal1.insert(0, line[0])
            diagonal2.append(line[-1])

            for i in range(1, len(line)):
                vertical[i] += line[i]
                diagonal1[i] += line[i]
            for i in range(j+1, j+len(line)):
                diagonal2[i] += line[i-j-1]
            j += 1
        
    print(findXMAS(horizontal) + findXMAS(vertical) + findXMAS(diagonal1) + findXMAS(diagonal2))
        

main()