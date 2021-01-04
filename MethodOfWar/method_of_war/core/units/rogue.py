from method_of_war.core.units.unit_models.a_unit import *


class Rogue(Unit):
    def __init__(self):
        super().__init__(isMelee=True, maxHp=600, armor=200, attackDamage=480, lootCapacity=100,
                         name="Rogue", resourceRequirement=ResourcesRequirementModel(30, 10, 30, 27),
                         movementSpeedInUnitsPerSecond=0.25)
