import math

class carScheduler(object):
    def __init__(self, *args):
        #print("Created", args)
        self.M = args[0][0] # Number of cars
        self.C = args[0][1] # capacity per car
        self.timestamps = args[0][2]
        self.N = len(self.timestamps) # number of people
        print("Cars: {0} Cap: {1} People Count: {2}".format(self.M, self.C, self.N))
        self.valid = True
        if (self.M * self.C < self.N):
            self.valid = False
            print("WARNING: Invalid scenario. # of cars * capacity/car >= # of people")


        self.searchResults = set()
        self.combos = []
    #    self.combos = self.validCombos()
        self.carAssignedCombos = []
        self.waitTimes = []
        self.waitTimeToCombo = dict()

    def searchCombinations(self):
        self.allLexicographic(self.getStringForLexi(), self.M)



    def isValidScenario(self):
        return self.valid

    def testWaitTime(self):
        self.highestWaitTimeIn(self.carAssignedCombos[0])

    def freshPeeps(self):
        return [x for x in range(self.N)]

    def highestWaitTimeIn(self, assignments):
        highest = -1
        for car, persons in assignments.items():
            prev = self.timestamps[persons[0]]
            totalWaitTime = 0
            for personIdx in persons:
                time = self.timestamps[personIdx]
                totalWaitTime+= time - prev
                prev = time

            if (totalWaitTime > highest):
                highest = totalWaitTime

        return highest

    def getLowestWaitTimeCombo(self):
        waitTimeKeys = sorted(self.waitTimeToCombo)
        #print(waitTimeKeys)
        lowestComboKey = waitTimeKeys[0]
        #print(lowestComboKey)
        print("timestamps: ", self.timestamps)

        return lowestComboKey, self.waitTimeToCombo[lowestComboKey]

    def mapMaxWaitTimes(self):
        print("processing: Calculating wait times.")
        for combo in self.carAssignedCombos:
            waitTime = self.highestWaitTimeIn(combo)
            self.waitTimeToCombo[waitTime] = combo
        print("Done.")
        #print(self.waitTimeToCombo)


    def assignCars(self):
        print("processing: Assigning cars to people.")
        for combo in self.combos:
            people = self.freshPeeps()
            people.reverse() # otherwise peeps will be added in reverse...
            carSet = dict()
            carIdx = 0
            for carCap in combo:
                cap = int(carCap)
                while (cap > 0):
                    p = people.pop()
                    if carIdx in carSet.keys():
                        carSet[carIdx].append(p)
                    else:
                        carSet[carIdx] = [p]
                    cap-=1
                carIdx+=1
            self.carAssignedCombos.append(carSet)
        print("Done.")

        #print(self.carAssignedCombos)

    def toString(self, s):
        return ''.join(s)


    def allLexicographic(self, s, l):
        print("processing: Finding all valid combinations.")
        data = [""] * (l+1)
        self.allLexicographicRecur(s, data, l-1, 0)
        print("Done.")

    def allLexicographicRecur(self, string, data, last, idx):
        length = len(string)

        for i in range(length):
            data[idx] = string[i]
            if idx == last:
                combo = self.toString(data)
                if (self.isValidCombo(combo)):
                    self.combos.append(combo)
            else:
                self.allLexicographicRecur(string, data, last, idx+1)


    def isValidCombo(self, combo):
        return int(math.fsum([int(x) for x in combo])) == self.N

    def getStringForLexi(self):
        s = ""
        for i in range(self.C+1):
            s+=str(i)
        return s


if __name__ == "__main__":
    """
    test format = (number of cars, capacity/cars, timestamps)
    """
    tests = [(4, 2, [1,2,5,7,8]),
    (2, 1, [1,2,5,7,8]),
    (5, 3, [1,2,5,7,11,12]),
    (5,2, [1,2,3,6,6,9,11,19]),
    (10,4, [1,2,3,6,6,9,11,19, 44, 47, 53, 192, 200, 204, 402]),
    (7,4, [1,2,3,6,6,9,11,19, 44, 47, 53, 192, 200, 204, 402]),
    (10,2, [1,2,3,40,43,59,93,99,123,153,155,165,169,170,180])
    ]

    for args in tests:
        print("*"*50)
        print("Starting test " )
        print("*"*50)

        scheduler = carScheduler(args)
        if (scheduler.isValidScenario()):
            scheduler.searchCombinations()
            scheduler.assignCars()
            scheduler.mapMaxWaitTimes()
            print("="*50)
            result = scheduler.getLowestWaitTimeCombo()
            print("(max wait time, car idx : [people idxs])")
            print(result)
            print("="*50)
