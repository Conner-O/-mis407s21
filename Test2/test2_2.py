with open('words.txt') as inputFile: #C:\MIS407\mis407s21-student-15\Test2\words.txt I had to use this path to make my program work

    count = 0
    total = 0

    for line in inputFile:
        count += 1
        total += len(line.strip())
        
    print("Number of words: ", count)
    print("Average word length: ", total / count)