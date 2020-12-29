
class ResourcesRequirementModel:
    woodValue: int
    graniteValue: int
    ironValue: int
    timeInSeconds: int

    def __init__(self, woodValue: int, graniteValue: int, ironValue: int, timeInSeconds: int):
        self.woodValue = woodValue
        self.graniteValue = graniteValue
        self.ironValue = ironValue
        self. timeInSeconds = timeInSeconds
