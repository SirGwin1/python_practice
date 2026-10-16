import random

class Weapon:
    def __init__(self, name, bonus_damage):
        self.name = name
        self.bonus_damage = bonus_damage

class Character:
    """The base class representing any living entity in the game."""
    def __init__(self, name, health, base_attack):
        self.name = name
        self.health = health
        self.base_attack = base_attack
        self.weapon = None  # Characters start unarmed
