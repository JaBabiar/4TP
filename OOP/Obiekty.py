class Character:
    def __init__(self, name, combat_class, inventory, lvl, gold, hp):
        self.name = name
        self.combat_class = combat_class
        self.inventory = inventory
        self.lvl = lvl
        self.gold = gold
        self.hp = hp

    def check_inventory(self):
        return self.inventory

    def take_dmg(self, dmg):
        if self.hp <= 0:
            return "Already dead!"

        self.hp -= dmg
        print(f"{self.name} took {dmg} dmg! {self.hp} left")

        if self.hp <= 0:
            self.hp = 0
            return f"{self.name} slain"

        return f"{self.name} has {self.hp}HP left"



class Archer(Character):
    def __init__(self, name, inventory, lvl, gold, hp, arrows):
        super().__init__( name, "Archer", inventory, lvl, gold, hp)
        self.arrows = arrows

    def bow_attack(self, target):
        self.arrows -= 1
        if self.arrows > 0:
            target.take_dmg(50)
        else:
            print("No more arrows")

        print(f"{self.arrows} Left")



class Mage(Character):
    def __init__(self, name, inventory, lvl, gold, hp):
        super().__init__( name, "Mage", inventory, lvl, gold, hp)





Lebron = Mage("Lebron", ["wand", "Hat"], 67, 1000, 320)
JeremySochan = Archer("Jeremy Sochan", ["Bow", "knife"], 25, 123, 250, 3)
print(Lebron.name, Lebron.combat_class, Lebron.hp)
print(JeremySochan.name, JeremySochan.combat_class, JeremySochan.hp)

JeremySochan.bow_attack(Lebron)
print(Lebron.name, Lebron.combat_class, Lebron.hp)
    


