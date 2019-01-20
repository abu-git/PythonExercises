"""
Create a function that returns the name of the winner in a fight between two fighters.

Each fighter takes turns attacking the other and whoever kills the other first is victorious. Death is defined as having health <= 0.

Each fighter will be a Fighter object/instance. See the Fighter class below in your chosen language.

Both health and damagePerAttack (damage_per_attack for python) will be integers larger than 0. You can mutate the Fighter objects.
"""
class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

    def __str__(self): return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)
    __repr__=__str__


def declare_winner(fighter1, fighter2, first_attacker):
	turn = first_attacker
	while(fighter1.health > 0 and fighter2.health > 0):
		if(fighter1.name == turn):
			fighter2.health = fighter2.health - fighter1.damage_per_attack
			turn = fighter2.name
		elif(fighter2.name == turn):
			fighter1.health = fighter1.health - fighter2.damage_per_attack
			turn = fighter1.name
	if(fighter1.health > 0):
		return fighter1.name
	elif(fighter2.health > 0):
		return fighter2.name



print(declare_winner(Fighter("Lew", 10, 2),Fighter("Harry", 5, 4), "Lew"))