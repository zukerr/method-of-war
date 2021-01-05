from method_of_war.core.units.unit_models.a_unit import *


class Warrior(Unit):
    def __init__(self):
        super().__init__(isMelee=True, maxHp=1000, armor=300, attackDamage=430, lootCapacity=30,
                         name="Warrior", resourceRequirement=ResourcesRequirementModel(60, 80, 100, 7),
                         movementSpeedInUnitsPerSecond=0.1)
