
class calculate:
    def __init__(self):
        self.FA = None
        self.UV = None

    def calculateValues(self, Area, SunGain, Factor):
        return Area * SunGain * Factor

    def calculate_FA(self, people, freash_air, floor_area):
        self.FA = people * freash_air + 0.6 * floor_area
        return self.FA

    def calculate_UV(self, height, floor_area, air_ch_required):
        self.UV = (height * floor_area * air_ch_required) / 60
        return self.UV

    def calculate_FAInput(self):
        return self.UV if self.UV > self.FA else self.FA

