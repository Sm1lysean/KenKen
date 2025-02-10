# KenKen
# The function that gives the user instructions
def help():
    print("This program only works for a 9x9 KenKen.")
    print("If you can change it, feel free to do so.")
    print("If you can't, I wouldn't suggest touching my spaghetti code.")
    input("Press enter to continue.\n")
    print("You need to continue entering values until you do them all.")
    print("After your done, enter 'quit' into the operation prompt.")
    input("Press enter to continue.\n")
    print("The first thing it will ask is for the 'Operation'.")
    print("This is the operation that appears in the top left of that box.")
    input("Press enter to continue.\n")
    print("The second thing it will ask is the 'Number'.")
    print("This is the number in the top left next to the operation.")
    input("Press enter to continue.\n")
    print("The third thing it will ask is the 'Boxes'.")
    print("This is how long the chain is including around corners.")
    input("Press enter to continue.\n")
    print("The forth thing it will ask is the 'Duplicates'.")
    print("This refers to how many times a number can be repeated.")
    print("This case happens when there is a corner.")
    input("Press enter to continue.\n")
    print("The best way to figure out what to put here is to count the number of\ncorners, then add one.")
    print("For example, if there are 2 corners, you would enter 3 in the 'Duplicates'")
    input("Press enter to continue.\n")
    print("The output after all the code is completed needs to be read.")
    input("Press enter to continue.\n")
    print("It will print something like this:")
    print("15× : ['135']\n15× : ['135']\n15× : ['135']\n\n9+ : ['18', '27', '36', '45']\n9+ : ['18', '27', '36', '45']\n\n8- : ['19']\n8- : ['19']")
    print("\nThe best way to read it is the first list is a box, the next is a differentbox in the chain.")
    print("It prints like this because it is easy to change after printing on paper.")
    input("Press enter to continue.\n")
    print("Now that you have read the instructions, you can start the code.")
    print("Click the 'Run' button again.")
    exit()

# This is the function that makes a list of all the solutions to a given situation.
def block(op, num, tiles, dupes):
    #Initialization steps
    tiles = int(tiles)
    list = []
    case = []
    ans = ""
    tot = 0
    #Creates Case[]
    for i in range(tiles):
        case.append(1)
    #Change the next digit by one if the previous one is 9. The same way base change is done.
    for i in range(9 ** (tiles) + 1):
        #Makes the digits 1-9 only
        for i in range(tiles - 1):
            if case[i] == 10:
                case[i] = 1
                case[i + 1] = int(case[i + 1]) + 1
        if case[tiles - 1] == 10:
            break
        #Non-Duplicate numbers
        #Checks each number individually and adds a counter for each unique number.
        count = 0
        if 1 in case:
            count += 1
        if 2 in case:
            count += 1
        if 3 in case:
            count += 1
        if 4 in case:
            count += 1
        if 5 in case:
            count += 1
        if 6 in case:
            count += 1
        if 7 in case:
            count += 1
        if 8 in case:
            count += 1
        if 9 in case:
            count += 1
        #Ordering numbers in case[] from least to greatest (used for De-Dupe later)
        sorted_case = sorted(case)
        #Checking if the case fits in the block
        ans = ""
        tot = 0
        for i in range(tiles):
            #Makes ans the string of sorted_case
            ans = ans + str(sorted_case[i])
        if op == "add" or op == "+":
            for i in range(tiles):
                #Makes tot the sum of sorted_case
                tot = tot + int(case[i - 1])
            op = "+"
        elif op == "mult" or op == "×":
            tot = 1
            for i in range(tiles):
                tot = tot * int(case[i - 1])
            op = "×"
        elif op == "sub" or op == "-":
            for i in range(tiles):
                tot = sorted_case[1] - sorted_case[0]
            op = "-"
        elif op == "div" or op == "÷":
            for i in range(tiles):
                tot = sorted_case[1] / sorted_case[0]
            op = "÷"
        elif op == "one" or op == "Box":
            op = "Box"
        else:
            raise Exception("")
        #Checks 3 things
        #1. If the total matches the number correctly
        #2. If the number has an allowed amount of duplicate numbers
        #3. If the number is not a duplicate
        if tot == int(num) and count >= tiles + 1 - int(dupes) and ans not in list:
            list.append(ans)
        #Adds one to the next run through, it could up by one as if it were a 4 digit number
        a = int(case[0]) + 1
        case[0] = a
    if op == "Box":
        comb = op + ": ['" + num + "']"
    else:
        comb = num + op + ": " + str(list)
    #Gives list[] back to the main program so it can be added to KenKen[]
    return comb


#Initialization
KenKen = []
list = []
op = ""
num = 0
boxes = 0
dupes = 0
print("Enter 'quit' to stop and 'help' for instructions.")

while True:
    op = input("Operation: ")
    if op == "quit":
        break
    if op == "help":
        help()
    num = input("Number: ")
    boxes = input("Boxes: ")
    dupes = input("Duplicates: ")
    try:
        comb = block(op, num, boxes, dupes)
    except:
        print("Something messed up, try again")
    else:
        for i in range(int(boxes)):
            KenKen.append(comb)
        KenKen.append("Break")
for i in range(len(KenKen)):
    if KenKen[i] == "Break":
        print("")
    else:
        print(KenKen[i])
