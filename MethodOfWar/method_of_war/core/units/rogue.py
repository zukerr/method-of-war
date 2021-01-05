from method_of_war.core.units.unit_models.a_unit import *


class Rogue(Unit):
    def __init__(self):
        super().__init__(isMelee=True, maxHp=600, armor=200, attackDamage=480, lootCapacity=100,
                         name="Rogue", resourceRequirement=ResourcesRequirementModel(80, 60, 80, 22),
                         movementSpeedInUnitsPerSecond=0.25)
