from method_of_war.core.units.unit_models.a_unit import *


class Hunter(Unit):
    def __init__(self):
        super().__init__(isMelee=False, maxHp=500, armor=70, attackDamage=450, lootCapacity=70,
                         name="Hunter", resourceRequirement=ResourcesRequirementModel(40, 10, 30, 20))
