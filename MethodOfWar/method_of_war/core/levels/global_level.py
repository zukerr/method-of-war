globalSettlementsList = []


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
