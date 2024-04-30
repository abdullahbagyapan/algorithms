"""
    @brief          Find locker doors that opened

    @param[n]       the number that n lockers exists

    @return         the list of number that locker door is open
"""
def lockerDoors(n):

    openDoorList = []

    totalVisitCount = 1

    while (totalVisitCount != n):

        # closed door
        if (totalVisitCount % 2 == 0):
            
            totalVisitCount += 1
            continue

        # open door
        openDoorList.append(n - totalVisitCount  + 1)
        
        totalVisitCount += 1

    return openDoorList


print(lockerDoors(10))

"""
The problem can be found on searching as "The locker doors problem"
"""