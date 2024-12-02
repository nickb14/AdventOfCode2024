#references

#same logic as part 1
def valid(report):
    diff = report[1] - report[0]
    if diff > 0:
        for i in range(1, len(report)):
            diff = report[i] - report[i-1]
            if diff <= 0 or diff > 3:
                return False
    elif diff < 0:
        for i in range(1, len(report)):
            diff = report[i] - report[i-1]
            if diff >= 0 or diff < -3:
                return False
    elif diff == 0:
        return False
    return True

def main():

    total = 0

    with open("day02/input.txt") as file:
        for line in file:
            report = [int(x) for x in line.split()]

            #if you remove the level at index i and it's still valid, you are good for that report
            for i in range(len(report)):
                if valid(report[:i] + report[i+1:]):
                    total += 1
                    break
    
    print(total)

main()


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#like, a really bad attempt
#ignore all of this
def badAttempt():

    total = 0

    with open("day02/input.txt") as file:
        for line in file:
            report = [int(x) for x in line.split()]

            diffs = [report[i]-report[i-1] for i in range(1, len(report))]

            bad, pos, neg = [], [], []
            for i in range(len(diffs)):
                if diffs[i] == 0 or abs(diffs[i]) > 3:
                    bad.append(i)
                elif diffs[i] > 0:
                    pos.append(i)
                else:
                    neg.append(i)

            if len(bad) == 0 and (len(pos) == 0 or len(neg) == 0):
                total += 1
            
            elif len(bad)+len(pos) <= 2:
                bad += pos
                if len(bad) == 2:
                    bad.sort()
                    if bad[1]-bad[0] == 1:
                        diff = diffs[bad[1]] + diffs[bad[0]]
                        if diff < 0 and diff >= 3:
                            total += 1
                elif len(bad) == 1:
                    if bad[0] != 0:
                        diff = diffs[bad[0]] + diffs[bad[0]-1]
                        if diff < 0 and diff >= -3:
                            total += 1
                            continue
                    if bad[0] != len(diffs)-1:
                        diff = diffs[bad[0]+1] + diffs[bad[0]]
                        if diff < 0 and diff >= -3:
                            total += 1
                            continue

            elif len(bad)+len(neg) <= 2:
                bad += neg
                if len(bad) == 2:
                    bad.sort()
                    if bad[1]-bad[0] == 1:
                        diff = diffs[bad[1]] + diffs[bad[0]]
                        if diff > 0 and diff <= 3:
                            total += 1
                elif len(bad) == 1:
                    if bad[0] != 0:
                        diff = diffs[bad[0]] + diffs[bad[0]-1]
                        if diff > 0 and diff <= 3:
                            total += 1
                            continue
                    if bad[0] != len(diffs)-1:
                        diff = diffs[bad[0]+1] + diffs[bad[0]]
                        if diff > 0 and diff <= 3:
                            total += 1
                            continue
    
    print(total)