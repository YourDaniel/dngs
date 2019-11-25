from ansi_wraps import Color


class Item:
    def __init__(self, name, rarity, quality, wear, material, damage, cost):
        self.color = Color.white
        self.cost = cost
        self.quality = quality
        self.quality_char = ''
        self.map_quality_char()
        self.name_unc = self.quality_char + name + self.quality_char    # name uncolored
        self.rarity = rarity
        self.map_color()
        self.name = self.color + self.name_unc + Color.reset

        self.damage = damage
        self.wear = wear
        self.material = material

    def map_quality_char(self):
        if self.quality == 'terrible':
            self.quality_char = '-'
        elif self.quality == 'poor':
            self.quality_char = '='
        elif self.quality == 'decent':
            self.quality_char = '~'
        elif self.quality == 'fine':
            self.quality_char = '≈'
        elif self.quality == 'good':
            self.quality_char = '•'
        elif self.quality == 'perfect':
            self.quality_char = '#'
        elif self.quality == 'masterpiece':
            self.quality_char = '☼'

    def map_color(self):
        if self.rarity == 'common':
            self.color = Color.l_black
        elif self.rarity == 'ordinary':
            self.color = Color.l_white
        elif self.rarity == 'uncommon':
            self.color = Color.l_green
        elif self.rarity == 'original':
            self.color = Color.cyan
        elif self.rarity == 'rare':
            self.color = Color.l_blue
        elif self.rarity == 'unique':
            self.color = Color.l_magenta
        elif self.rarity == 'legendary':
            self.color = Color.yellow
        elif self.rarity == 'mythic':
            self.color = Color.red

    def calculate_damage(self):
        self.base_dmg

    def print_description(self):
        pass

