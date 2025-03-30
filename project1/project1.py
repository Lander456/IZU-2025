import math

def newCoordGen(xDiff, yDiff, oldX, oldY):

    newCoord = []

    if ((xDiff + oldX) >= lowerLimit) and ((xDiff + oldX) <= upperLimit):

        newCoord.append(xDiff + oldX)

        if ((yDiff + oldY) >= lowerLimit) and ((yDiff + oldY) <= upperLimit):

            newCoord.append(yDiff + oldY)

        else:

            newCoord = []
    
    return newCoord

openQ = []
closed = []
start = ([1, 4], None, 0, 3, 3)
goal = [6, 4]
iteration = 0
lowerLimit = 0
upperLimit = 7
moves = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]]

file = open("result.md", "w")

openQ.append(start)

lowestItem = openQ[0]

while(lowestItem[0] != goal):

    file.write("iteration number {0}\nopenQ:\n{1}\nClosed:\n{2}\n".format(iteration, openQ, closed))

    iteration += 1

    lowestItem = None

    for item in openQ:

        if lowestItem == None:

            lowestItem = item
            continue

        if item[4] < lowestItem[4]:

            lowestItem = item

    oldX = lowestItem[0][0]
    oldY = lowestItem[0][1]

    closed.append(openQ.pop(openQ.index(lowestItem)))

    visited = False

    for move in moves:

        newCoord = newCoordGen(move[0], move[1], oldX, oldY)

        if newCoord != []:

            for oldMove in closed:

                if newCoord == oldMove[0]:

                    visited = True

            for item in openQ:

                if newCoord == item[0]:

                    visited = True

            if visited:

                visited = False
                continue

            moveNum = lowestItem[2] + 1

            heuristic = max(abs(newCoord[0] - goal[0]) / 2, abs(newCoord[1] - goal[1]) / 2)

            heuristic = int(math.ceil(heuristic))

            openQ.append((newCoord, lowestItem[0], moveNum, heuristic, heuristic + moveNum))

closed.append(lowestItem)

path = []

parentRoot = lowestItem[1]

path.append(lowestItem[0])

while parentRoot != None:

    for item in closed:

        if item[0] == parentRoot:

            parentRoot = item[1]
            path.append(parentRoot)

print(path)