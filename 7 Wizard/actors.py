import random
import collections


# TODO get_defensive_roll => get_defensive_role

fightstatus = collections.namedtuple('fightstatus', 'damage, result')

class Creature(object):  # default class bepalen met de benodige variablen


    def __init__(self, bonus=None, strengt=None, name=None, level=None, behaviour=None, loot=None):
        self.bonus = bonus if bonus is not None else 5
        self.strengt = strengt if strengt is not None else random.randint(10, 15)
        self.name = name if name is not None else random.choice(['Tiger', 'Lion', 'Bear'])
        self.level = level if level is not None else random.randint(8, 12)
        self.behaviour = behaviour if behaviour is not None else random.randint(1, 8)
        self.loot = loot if loot is not None else random.randint(1, 8)

    def __repr__(self):
        return "Creature {} of level {}".format(
            self.name, self.level
        )

    def get_defensive_roll(
            self):  # bepalen van de aanvallen voor alle spelers, inclusief de hero, dat is namelijk ook gewoon een creature
        return random.randint(1, 12) * self.strengt


class Wizard(Creature):
    _fight_status = {
        'truce': 0,
        'flee': 1,
        'win': 2,
        'killed': 3
    }
    @staticmethod
    def get_fight_status(status):
        if isinstance(status, int):
            for key, value in Wizard._fight_status:
                if status == value:
                    return key
            return None

        return Wizard._fight_status.get(status, None)


    # alleen de held (Wizard) kan een aanval bepalen (gelukkig)
    def attack(self, creature):
        print('The wizard {} with {} health and a power of {}, attacks {} with {} strengt and a power of {}!'.format(
            self.name,
            self.level,
            self.strengt,
            creature.name,
            creature.level,
            creature.strengt
        ))

        my_roll = self.get_defensive_roll()
        creature_roll = creature.get_defensive_roll()
        print('You roll {}'.format(my_roll))
        print('{} roll {}'.format(creature.name, creature_roll))

        fightstatus.damage = 0
        fightstatus.result = Wizard.get_fight_status("truce")

        # kijken of eventueel een smallanimal vlucht
        if not creature_roll:
            fightstatus.result = Wizard.get_fight_status("flee")
            return fightstatus

        creature.level -= self.strengt
        if my_roll >= creature_roll:
            print('{} has defeated {}'.format(self.name, creature.name))

            if creature.level <= 0:
                print('{} has been killed'.format(creature.name))
                fightstatus.result = Wizard.get_fight_status("win")
            else:
                print('{} now has a health of {}'.format(creature.name, creature.level))


        else:

            fightstatus.damage = creature_roll
            if creature.level <= 0:
                print(
                    '{} has been killed, but manged to do you {} harm, no bonus has been awarded.'.format(creature.name,
                                                                                                          creature_roll))
                fightstatus.result = Wizard.get_fight_status("killed")
            else:
                print('{} now has a health of {}'.format(creature.name, creature.level))
                print('{} has hid you and takes {} of your health'.format(creature.name, creature_roll))
        return fightstatus



class SmallAnimal(Creature):
    def __init__(self, name=None):
        super().__init__(
            name=(name if name is not None else random.choice(['Toad','Bat', 'Mouse', 'Rat', 'Spider', 'Bunny', 'Frog', 'Wasp', 'Bee'])),
            bonus=1,
            strengt=random.randint(1, 2),
            level=random.randint(1, 4),
            behaviour=random.randint(1, 8),
            loot=random.randint(1, 8))

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        if random.choice([True, False]):
            print('the creature has run away')
            return 0
        else:
            return int(base_roll / 2)  # ik wil geen halve waardes dus maak ik er expliciet een integer van (python maakt er anders een float van door de delen door)


class Dragon(Creature):

    def __init__(self, breaths_fire=None):
        super().__init__(
            name='Dragon',
            bonus=10,
            strengt= random.randint(25, 75),
            level= random.randint(40, 60),
            behaviour=9,
            loot=random.randint(10, 25)

        )
        self.scaliness = 75
        self.breaths_fire = breaths_fire if breaths_fire is not None else random.choice([True,False])

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        fire_modifier = 5 if self.breaths_fire else 1
        scale_modifier = self.scaliness / 10
        return int(base_roll * fire_modifier * scale_modifier)
