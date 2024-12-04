def main():

    lines = []

    with open("day04/input.txt") as file:
        for line in file:
            lines.append(line)
    
    total = 0

    #I think a more elegant solution comapred to part 1
    #just loops through the whole board once and looks for the XMAS pattern
    #  looks for A's first, then looks if it is correctly surrounded by M's and S's
    for i in range(1, len(lines)-1):
        for j in range(1, len(lines[i])-1):
            if lines[i][j] == 'A':
                if lines[i-1][j-1] == 'S' and lines[i+1][j-1] == 'S' and lines[i+1][j+1] == 'M' and lines[i-1][j+1] == 'M':
                    total += 1
                elif lines[i-1][j-1] == 'M' and lines[i+1][j-1] == 'S' and lines[i+1][j+1] == 'S' and lines[i-1][j+1] == 'M':
                    total += 1
                elif lines[i-1][j-1] == 'M' and lines[i+1][j-1] == 'M' and lines[i+1][j+1] == 'S' and lines[i-1][j+1] == 'S':
                    total += 1
                elif lines[i-1][j-1] == 'S' and lines[i+1][j-1] == 'M' and lines[i+1][j+1] == 'M' and lines[i-1][j+1] == 'S':
                    total += 1
    
    print(total)

        

main()