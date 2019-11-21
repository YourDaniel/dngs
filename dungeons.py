from random import choice
from random import randint
from readchar import readkey
from items import Item
from ansi_wraps import print_colored
import json
import ctypes
kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

with open('weapons.json', 'r', encoding='UTF-8-sig') as file:
    weapons = json.load(file)

# gray, white, light green, yellow, blue, purple, orange, red
rarity = {'common': 0.8, 'ordinary': 1, 'uncommon': 1.2, 'original': 1.8, 'rare': 2, 'unique': 2.4, 'legendary': 3, 'mythic': 3.5}
# TODO: RARE things cant be bad quality or broken
# TODO: tune random chances of things
wear = {'broken': 0.4, 'worn': 0.8, 'used': 1, 'new': 1.2}
quality = {'terrible': 0.5, 'poor': 0.8, 'fine': 1, 'decent': 1.2, 'good': 1.4, 'perfect': 1.8, 'epic': 2.4, 'masterpiece': 3}
#weapon = {'dagger': 15, 'sword': 30, 'longsword': 50, 'mace': 50, 'axe': 20, 'flail': 35, 'tomahawk': 25, 'halberd': 50, 'battle axe': 60, 'club': 10, 'pike': 15, 'spear': 40}
armor_material = ['cloth', 'fur', 'leather', 'iron', 'steel', 'black steel', 'gold', 'mythril', 'adamantine', 'silver']
animals = ['bear', 'fox', 'wolf', 'cave spider', 'dragon', 'elephant', 'marten', 'arctic fox', 'squirrel', 'sable']
armor_piece = ['left boot', 'right boot', 'left gauntlet', 'right gauntlet', 'pants', 'shirt', 'leg armor', 'body armor', 'shoulder pad', 'helmet']


'''
class Inventory:
    inventory = []
    weapon_equipped = 0
    def add_item(self, item):
        inventory.append(item)

    def remove_item(self, item):
        inventory.remove(item)
    
    def equip_item(self, item):
    def deequip_item():
        
class Rogue:
    def __init__(self, name, class_name):
        self.name = name
        self.class_name = 'Rogue'
'''


class Hero:
    def __init__(self, max_hp, attack):
        self.max_hp = max_hp
        self.attack = attack
        self.hp = self.max_hp
        self.equipped_weapon = None
        self.weapons = []

    def fight_monster(self, monster):
        while True:
            monster.hp -= self.attack
            print(f'You hit monster for {self.attack} damage. HP left {monster.hp}')
            if monster.hp <= 0:
                print(f'You defeated {monster.name}')
                return True
            self.hp -= monster.attack
            print(f'Monster hit you for {monster.attack} damage. HP left {self.hp}')
            if self.hp <= 0:
                self.hp = 0
                print(f'{monster.name} defeated you!')
                return False

    def equip_weapon(self):
        self.print_weapons()
        wpn_n = int(input())
        self.attack = self.weapons[wpn_n-1].damage
        print(f'Weapon equipped! Your attack now: {self.attack}')

    def add_weapon(self, weapon):
        self.weapons.append(weapon)

    def print_weapons(self):
        for i in range(len(self.weapons)):
            name = self.weapons[i].name
            dmg = self.weapons[i].damage
            clr = self.weapons[i].color
            print(i+1, end=' ')
            print_colored(name, clr)
            print(f'. DMG: {dmg}')


class Enemy:
    def __init__(self, hp, attack):
        self.name = self.generate_name()
        self.hp = hp
        self.attack = attack

    def generate_name(self):
        adjectives = ['scary', 'bone', 'horrible', 'putrid', 'bloodthirsty', 'death', 'old', 'dark', 'fierce', 'horror', 'hell', 'venomous', 'doom', 'furious']
        monsters = ['frog', 'blob', 'bear', 'fairy', 'snake', 'minotaur', 'spider', 'bat', 'abomination', 'slug', 'rat', 'ooze'] + animals
        name = choice(adjectives).capitalize() + ' ' + choice(monsters).capitalize()
        return name
    

class Loot:
    def generate_weapon(self):
        rar = choice(list(rarity))
        wr = choice(list(wear))
        qual = choice(list(quality))
        mat = choice(list(armor_material))
        wpn_n = randint(0, len(weapons['weapons']) - 1)
        cost_value = weapons['weapons'][wpn_n]['cost']
        cost = cost_value * quality[qual] * wear[wr] * rarity[rar]
        weapon_name = rar.capitalize() + ' ' + weapons['weapons'][wpn_n]['name']
        weapon = Item(weapon_name, rar, qual, wr, mat, weapons['weapons'][wpn_n]['damage'])
        print(f"You've got", end=' ')
        print_colored(weapon_name, weapon.color)
        print(f' of {qual} quality! It is {wr}. Cost: {int(cost)}')
        return weapon


    def generate_armor(self):
        rar = choice(list(rarity))
        wr = choice(list(wear))
        qual = choice(list(quality))
        arm = choice(list(armor_piece))
        mat = choice(list(armor_material))
        print(f"You've got {rar} {mat} {arm} of {qual} quality! It is {wr}.")
        return rar + ' ' + arm

        
def main():
    #name = input('Enter your name: ')
    loot = Loot()
    inventory = []
    hero = Hero(10, 1)
    monsters = [Enemy(randint(3, 12) + i*10, i+1) for i in range(10)]
    lives = 3
    monster_id = 0
    print(f'You are mighty hero! HP: {hero.hp}. ATTACK: {hero.attack}')
    while True:
        while True:
            action = input('What should I do?')
            if action == 'e':
                print('Equip what?')
                hero.equip_weapon()
                break
            elif action == 'g':
                print('Going into the next room!')
                break
        print(f'You encountered {monsters[monster_id].name}!')
        if hero.fight_monster(monsters[monster_id]):
            atk = randint(0, 1)
            hp = randint(15, 30)
            #hero.max_hp += hp
            hero.hp += hp
            hero.attack += atk
            print(f'You gained {atk} attack and healed for {hp} hp!')
            coin =  1 #randint(0, 1)
            if coin == 0:
                inventory.append(loot.generate_armor())
            else:
                hero.add_weapon(loot.generate_weapon())

            if len(monsters) - 1 == monster_id:
                print('You have cleared the dungeon!')
                print('Your loot:')
                hero.print_weapons()
                break
            else:
                monster_id += 1
        else:
            print('Try again!')
            hp = randint(5, 20)
            hero.hp += hp
            print(f'You healed for {hp} hp!')
main()
