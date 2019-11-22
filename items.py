from ansi_wraps import Color

class Item:
    def __init__(self, name, rarity, quality, wear, material, damage):
        self.quality = quality

        # - = ~ ≈ • ○ ☼
        if self.quality == 'terrible':
            qual_char ='-'
        elif self.quality == 'poor':
            qual_char ='='
        elif self.quality == 'decent':
            qual_char = '~'
        elif self.quality == 'fine':
            qual_char ='≈'
        elif self.quality == 'good':
            qual_char ='•'
        elif self.quality == 'perfect':
            qual_char ='#'
        elif self.quality == 'masterpiece':
            qual_char ='☼'
        else:
            qual_char = ''
        self.name_unc = qual_char + name + qual_char # name uncolored
        self.rarity = rarity
        self.damage = damage
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
        else:
            self.color = Color.white
        self.name = self.color + self.name_unc + Color.reset

        self.wear = wear
        self.material = material

    def print_description(self):
        pass

