import random
import time
import Header
import collections
from actors import Wizard, Creature, SmallAnimal, Dragon



SURPRISE_MODE = {
    1: "has appeared from a dark and foggy forest..",
    2: "sneaks up from your behind...",
    3: "jumps out of the bushes...",
    4: "run's right at you...",
    5: "appears from the mist...",
    6: "crawls out of a tunnel...",
    7: "looks surprised at you..",
    8: "wanders around..",
    9: "fly's down from the sky..."
}


fightstatus = collections.namedtuple('fightstatus', 'damage, result')

def main():
    Header.print_header(title='Wizard Battle App', bar='=')
    print('')
    player = input('Please give your Hero name: ')
    game_loop(player)


def game_loop(Hero_name):


    # de eindbaas is een Evil Wizard
    creatures = [
        Wizard(1000, 50, 'Evil Wizard', random.randint(500, 1500), 8, random.randint(1, 8))
    ]
    # de lijst met creatures aanvullen tot 5 met random gekozen creatures uit de lijst met alle mogelijkheden
    creatures = choice_creature(creatures, count=5)
    # de start waardes voor de Hero.
    hero_power = 500
    hero_strengt = 10
    money_bag = 5

    while hero_power >= 1:  # zolang de Hero leeft.
        hero = Wizard(1, hero_strengt, Hero_name, hero_power, 1, money_bag)  # hero zijn waardes doorgeven
        active_creature = random.choice(creatures)  # actieve creature kiezen
        surprise_mode = SURPRISE_MODE.get(active_creature.behaviour, None)


        if isinstance(active_creature, Dragon):  # draken komen altijd uit de lucht en spugen wel of geen vuur.

            print('A {}{} of level {} with a strengt of {} '.format(
                    ('Firebreathing ' if active_creature.breaths_fire else ''),
                    active_creature.name,
                    active_creature.level,
                    active_creature.strengt
            ))

        else:  # is het geen draak, dan wordt er nu gekeken hoe de creature tevoorschijn komt.
            print('A {} of level {} with a strengt of {} {} .'.format(
                active_creature.name,
                active_creature.level,
                active_creature.strengt,
                surprise_mode
            ))  # printen van het creature dat op welke manier tevoorschijn komt.
        print()
        cmd = True
        while cmd != "x":
            cmd = input(
                'Do you [A]ttack, [R]unaway and look for additional targets, [L]ook around and change target, go to the [S]hop or [X] to exit? '.format(
                    hero_power, hero_strengt))  # vragen wat we met het monster gaan doen.
            cmd = cmd.lower().strip()
            Header.print_header(
                title='Your Hero is: {} with {} strengt and an health of: {} and owns {} Gold'.format(hero.name, hero_strengt, hero_power, money_bag),
                bar='=')  # header printen met daarin onze waardes
            if cmd == 'a':  # aanval aanroepen in de actors module.
                fightstatus = hero.attack(active_creature)  # als we winnen wordt er win terug gegeven
                if fightstatus.result == Wizard.get_fight_status("win"):
                    money_bag += active_creature.loot
                    print('you have found {} Gold on {} You now have {} Gold'.format(active_creature.loot, active_creature.name, money_bag))
                    creatures.remove(active_creature)
                    if active_creature.bonus == 1:  # bonus bekijken en toekennen
                        hero_power += 10
                        print('Your hero gains 10 health and now has {}'.format(hero_power))
                    elif active_creature.bonus == 5:
                        hero_strengt += 5
                        print('Your hero gains 5 strengt and now has {}'.format(hero_strengt))
                    else:
                        hero_power += 100
                        print('Your hero gains 100 health and now has {}'.format(hero_power))
                    break
                elif fightstatus.result == Wizard.get_fight_status("killed"):
                    money_bag += active_creature.loot
                    print('you have found {} Gold on {} You now have {} Gold'.format(active_creature.loot, active_creature.name, money_bag))
                    creatures.remove(active_creature)
                    hero_power -= fightstatus.damage  # we hebben verloren, de aanval wordt van onze healt afgetrokken
                    if hero_power >= 1:  # overleven we de aanval verstoppen we ons en hebben we 5 sec nodig om te recoveren
                        print('{} runs and hides taking time to recover..'.format(hero.name))
                        time.sleep(5)
                        print('{} returns with a healt of {}'.format(hero.name, hero_power))
                    else:  # we zijn dood, Game Over
                        print('your level is to low to fight, GAME OVER')
                    break
                elif fightstatus.result == Wizard.get_fight_status("flee"):
                    creatures.remove(active_creature)
                    break
                else:
                    hero_power -= fightstatus.damage  # we hebben verloren, de aanval wordt van onze healt afgetrokken
                    if hero_power >= 1:  # overleven we de aanval verstoppen we ons en hebben we 5 sec nodig om te recoveren
                        print('{} runs and hides taking time to recover..'.format(hero.name))
                        time.sleep(5)
                        print('{} returns with a healt of {}'.format(hero.name, hero_power))
                    else:  # we zijn dood, Game Over
                        print('your level is to low to fight, GAME OVER')
                    break


            elif cmd == 'r':  # we rennen weg voor het monster of gaan opzoek naar nieuwe monsters om onze lijst aan te vullen.
                print("The wizard has become unsure of his power and run's away to look for new creatures !!!")
                for c in range(len(creatures), 5):  # aanvullen van de lijst
                    creatures = choice_creature(creatures, count=5)
                break


            elif cmd == 'l':  # printen van alle monsters en nieuw doel kiezen
                print('{} takes a look in the surroundings and sees a '.format(hero.name))
                for c in creatures:
                    print('* A {} of level {} with a strengt of {}'.format(c.name, c.level, c.strengt))
                break


            elif cmd == 's':
                shop = 9
                while shop != 0:
                    Header.print_header(title='Welkom in the shop you own {} Gold'.format(money_bag), bar='$')
                    print('1)  10 healt kost    5 gold')
                    print('2)  25 healt kost   10 gold')
                    print('3) 100 healt kost   30 gold')
                    print()
                    print('4)  5  strengt kost  5 gold')
                    print('5) 10  strengt kost  8 gold')
                    print('6) 25  strengt kost 18 gold')
                    print()
                    print('to exit the shop press 0')
                    print()
                    shop = int(input('please give the number of you choise'))
                    if shop == 1:
                        if money_bag - 5 < 0:
                            print('sorry you do not have enough Gold')
                            shop = 8
                        hero_power += 10
                        money_bag -= 5
                    elif shop == 2:
                        if money_bag - 10 < 0:
                            print('sorry you do not have enough Gold')
                            shop = 8
                        hero_power += 25
                        money_bag -= 10
                    elif shop == 3:
                        if money_bag - 30 < 0:
                            print('sorry you do not have enough Gold')
                            shop = 8
                        hero_power += 100
                        money_bag -= 30
                    elif shop == 4:
                        if money_bag - 5 < 0:
                            print('sorry you do not have enough Gold')
                            shop = 8
                        hero_strengt += 5
                        money_bag -= 5
                    elif shop == 5:
                        if money_bag - 8 < 0:
                            print('sorry you do not have enough Gold')
                            shop = 8
                        hero_strengt += 10
                        money_bag -= 8
                    elif shop == 6:
                        if money_bag - 18 <= 0:
                            print('sorry you do not have enough Gold')
                            shop = 8
                        hero_strengt += 25
                        money_bag -= 18



        else:
            print('OK, exiting game.... bye!')  # we hebben niets gekozen dus exit
            return hero, creatures

        if not creatures:  # als alle monsters zijn verslagen dus ook de eindbaas dan hebben we gewonnen
            print("You've defeated all the creatures, well done!")
            break
        print()

def choice_creature(creatures, count):
    nieuw_creatures = random.choices(
            [SmallAnimal, Creature, Dragon],
            [4, 2, 1],
            k=count-len(creatures)
        )
    creatures.extend([nc() for nc in nieuw_creatures])
    return creatures





if __name__ == '__main__':
    main()
