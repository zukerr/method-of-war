from method_of_war.core.units.unit_models.a_unit import *
from method_of_war.core.units.paladin import *
from method_of_war.core.units.warrior import *
from method_of_war.core.units.rogue import *
from method_of_war.core.units.hunter import *


__unitList = [
    Warrior(),
    Paladin(),
    Rogue(),
    Hunter()
]

__unitCreationList = [
    lambda: Warrior(),
    lambda: Paladin(),
    lambda: Rogue(),
    lambda: Hunter()
]


def MakeUnit(unitName: str):
    for i in range(len(__unitList)):
        unit = __unitList[i]
        if unit.getName() == unitName:
            return __unitCreationList[i]()
    return None
