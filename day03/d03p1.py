def main():

    total = 0

    with open("day03/input.txt") as file:
        file = file.read()
        
        #just loop through every character in the file
        for i in range(len(file)):
            if file[i:i+4] == 'mul(':
                comma = file.index(',', i)
                end = file.index(')', i)
                m1 = file[i+4:comma]
                m2 = file[comma+1:end]

                #if you find a valid mul(,) instruction with numeric values, add it to total
                if m1.isnumeric() and m2.isnumeric():
                    total += int(m1) * int(m2)
            
    
    print(total)

main()