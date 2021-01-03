from method_of_war.core.units.unit_models.a_unit import *


class Paladin(Unit):
    def __init__(self):
        super().__init__(isMelee=True, maxHp=900, armor=400, attackDamage=80, lootCapacity=30,
                         name="Paladin", resourceRequirement=ResourcesRequirementModel(10, 50, 30, 15),
                         movementSpeedInUnitsPerSecond=0.08)
