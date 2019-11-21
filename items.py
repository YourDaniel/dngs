class Item:
    def __init__(self, name, rarity, quality, wear, material, damage):
        self.name = name
        self.rarity = rarity
        self.quality = quality
        self.wear = wear
        self.material = material
        self.damage = damage
        if self.rarity == 'common':
            self.color = 'l_black'
        elif self.rarity == 'ordinary':
            self.color = 'l_white'
        elif self.rarity == 'uncommon':
            self.color = 'l_yellow'
        elif self.rarity == 'original':
            self.color = 'cyan'
        elif self.rarity == 'rare':
            self.color = 'blue'
        elif self.rarity == 'unique':
            self.color = 'magenta'
        elif self.rarity == 'legendary':
            self.color = 'yellow'
        elif self.rarity == 'mythic':
            self.color = 'red'
        else:
            self.color = 'white'

        # gray, white, light green, yellow, blue, purple, orange, red
        #rarity = {'common': 0.8, 'ordinary': 1, 'uncommon': 1.2, 'original': 1.8, 'rare': 2, 'unique': 2.4,
              #    'legendary': 3, 'mythic': 3.5}

