from method_of_war.core.units.unit_models.a_unit import *


class Hunter(Unit):
    def __init__(self):
        super().__init__(isMelee=False, maxHp=500, armor=150, attackDamage=500, lootCapacity=70,
                         name="Hunter", resourceRequirement=ResourcesRequirementModel(90, 60, 80, 15),
                         movementSpeedInUnitsPerSecond=0.2)
