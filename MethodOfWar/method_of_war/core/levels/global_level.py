globalSettlementsList = []
levelIsRunning = True
levelIsActive = True
__lateFunctionQueuedUp = False
lateFunction = lambda: None


def getSettlementByPosition(position: (int, int)):
    print("getSettlementByPosition: globalSettlementList: ")
    print(globalSettlementsList)
    for elem in globalSettlementsList:
        print("elem location: ")
        print(elem.getLocation())
        print("argument position: ")
        print(position)
        if elem.getLocation() == position:
            return elem
    return None


def executeLateFunction():
    global __lateFunctionQueuedUp
    if __lateFunctionQueuedUp:
        lateFunction()
        __lateFunctionQueuedUp = False
