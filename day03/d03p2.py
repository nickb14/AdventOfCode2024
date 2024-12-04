def main():

    total = 0

    with open("day03/input.txt") as file:
        file = file.read()
        
        #same as part 1, with an extra variable
        enabled = True
        for i in range(len(file)):
            if file[i:i+4] == 'mul(':
                comma = file.index(',', i)
                end = file.index(')', i)
                m1 = file[i+4:comma]
                m2 = file[comma+1:end]

                #only add to total if enabled is True (if there was a do())
                if enabled and m1.isnumeric() and m2.isnumeric():
                    total += int(m1) * int(m2)
            elif file[i:i+4] == 'do()':
                enabled = True
            elif file[i:i+7] == 'don\'t()':
                enabled = False
            
    
    print(total)

main()