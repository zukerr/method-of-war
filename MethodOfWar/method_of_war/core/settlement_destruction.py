from method_of_war.ui import global_gameplay_view_manager


class SettlementDestruction:
    __currentHealth: int
    __maxHealth: int
    __armor: int
    __location: (int, int)
    __isDestroyed: bool

    def __init__(self, location: (int, int), maxHealth: int = 1000, armor: int = 400):
        self.__maxHealth = maxHealth
        self.__currentHealth = self.__maxHealth
        self.__armor = armor
        self.__location = location
        self.__isDestroyed = False
        # self.updateMapUi()

    def modifyHealth(self, value: int):
        if value < 0:
            value = value + self.__armor
        self.__currentHealth += value
        if self.__currentHealth < 0:
            self.__currentHealth = 0
        if self.__currentHealth > self.__maxHealth:
            self.__currentHealth = self.__maxHealth

        if self.__currentHealth <= 0:
            self.__isDestroyed = True

        # update map ui
        self.updateMapUi()

    def getCurrentHealth(self) -> int:
        return self.__currentHealth

    def updateMapUi(self):
        healthPercentage: float = float(self.__currentHealth) / float(self.__maxHealth)
        healthText = str(self.__currentHealth) + "/" + str(self.__maxHealth)
        print(healthText)
        global_gameplay_view_manager \
            .globalGameplayViewManager \
            .getMapView() \
            .updateNodeProgressBar(self.__location[0], self.__location[1], healthPercentage, healthText)
