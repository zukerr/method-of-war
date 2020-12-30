from method_of_war.core.units.unit_models.a_unit import *


class Rogue(Unit):
    def __init__(self):
        super().__init__(isMelee=True, maxHp=600, armor=100, attackDamage=420, lootCapacity=100,
                         name="Rogue", resourceRequirement=ResourcesRequirementModel(30, 10, 30, 27))
