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
    def equip_weapon(self, weapon):
        self.weapon = weapon
        print(f"⚔️ {self.name} equipped {weapon.name}!")

    def attack(self, target):
        # Calculate total damage (Base attack + Weapon bonus if they have one)
        damage = self.base_attack
        if self.weapon:
            damage += self.weapon.bonus_damage
        
        print(f"💥 {self.name} attacks {target.name} for {damage} damage!")
        target.take_damage(damage)

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            print(f"💀 {self.name} has been defeated!")
        else:
            print(f"❤️ {self.name} has {self.health} HP left.")

class Player(Character):
    """Player inherits from Character but adds unique features like healing."""
    def __init__(self, name, health, base_attack, role):
        super().__init__(name, health, base_attack)  # Setup base character traits
        self.role = role
        self.potions = 2

    def heal(self):
        if self.potions > 0:
            self.health += 30
            self.potions -= 1
            print(f"🧪 {self.name} drank a potion and healed 30 HP! (Remaining: {self.potions})")
            print(f"❤️ Current HP: {self.health}")
        else:
            print("❌ No potions left!")

class Enemy(Character):
    """Enemy inherits from Character but has specific monster types."""
    def __init__(self, name, health, base_attack, species):
        super().__init__(name, health, base_attack)
        self.species = species

# --- THE GAME LOOP ---
if __name__ == "__main__":
    print("--- Welcome to OOP Python RPG ---")
    
    # 1. Create objects
    hero = Player(name="Arthur", health=100, base_attack=15, role="Knight")
    goblin = Enemy(name="Grog", health=60, base_attack=10, species="Goblin")
    
    sword = Weapon(name="Excalibur", bonus_damage=10)
    hero.equip_weapon(sword)
    
    print("\n--- The Battle Begins! ---")