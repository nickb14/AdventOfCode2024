#references

def main():

    total = 0

    with open("day02/input.txt") as file:
        for line in file:
            report = [int(x) for x in line.split()]
            
            diff = report[1] - report[0]
            #if the first difference is positive, all of the differences should be positive (less than 3)
            if diff > 0:
                for i in range(1, len(report)):
                    diff = report[i] - report[i-1]
                    if diff <= 0 or diff > 3:
                        break
                else:
                    total += 1
            #if the first difference is negative, all of the differences should be negative (greater than -3)
            elif diff < 0:
                for i in range(1, len(report)):
                    diff = report[i] - report[i-1]
                    if diff >= 0 or diff < -3:
                        break
                else:
                    total += 1
    
    print(total)

main()