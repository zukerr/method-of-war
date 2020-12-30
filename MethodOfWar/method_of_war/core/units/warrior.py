from method_of_war.core.units.unit_models.a_unit import *


class Warrior(Unit):
    def __init__(self):
        super().__init__(isMelee=True, maxHp=1000, armor=300, attackDamage=50, lootCapacity=30,
                         name="Warrior", resourceRequirement=ResourcesRequirementModel(10, 30, 50, 12))
