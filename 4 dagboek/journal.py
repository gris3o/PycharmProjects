'''
dit bestand doet puur de I/O regelen met de computer, en UI vind plaats in het Program.py gedeelte
'''

import os


# mbv import OS laden we de os specifieke functies denk aan / of \ slash verschil tussen windows en unix. of bij ping de -n of -p funcites

def load(name):
    """
    Hier wordt eerst een list aangemaakt, genaamt "data"
    Daarna wordt er gekeken of er een bestand bestaat met de naam die is ingevoerd.
    Als dit bestand bestaat wordt de inhoud van dit bestand weggeschreven in het de list "data"
    deze list wordt daarna terug gegeven naar de functie waar hij werd aangeroepen
    :param name: de naam van de gerbuiker die is ingegeven
    :return: een list genaamd data met daarin de gegevens van de gebruiker
    """
    # het maken van de list
    data = []
    # het volledige path van het bestand inladen in de variable filename
    filename = get_full_pathname(name)
    # nu kijken we of het bestand bestaat en als hij bestaat openen we hem.
    if os.path.exists(filename):
        # het bestand openen en de inhoud weg schrijven in fin (file input)
        with open(filename) as fin:
            # voor elke regel in fin wordt de onderstaande opdracht uitgevoerd
            for entry in fin.readlines():
                # elke regel wordt nu toegevoegd aan de list data. dit gebeurt mbv .append, door de rstrip worden eventuele spaties aan het begin weggehaald en enters verwijderd
                data.append(entry.rstrip())
    # nu wordt data terug gegeven aan de functie die deze functie heeft aangeroepen
    return data


def save(name, journal_data):
    """
    hier wordt de data weggeschreven in een bestand met de naam welke is opgegeven door de gebruiker
    :param name: de naam van de gebruiker die is ingegeven
    :param journal_data: de ingevoerde data en de eventueel al ingelade data vanuit de load functie
    :return: er wordt niets terug gegeven door deze functie
    """
    # het maken van de de bestandstructuur (hier hadden we het OS voor nodig)
    filename = get_full_pathname(name)
    # hier wordt geprint dat we aan het opslaan zijn met daarachter de locatie en de naam waar we opslaan
    print('....saving to: {}'.format(filename))
    # hier wordt het bestand geopend (mocht het nog niet bestaan wordt het hier ook aangemaakt) dit bestand wordt in python de variabke fout (file output)
    with open(filename, "w") as fout:
        # hier wordt voor elke waarde in de list de onderstaande actie uitgevoerd
        fout.write('\n'.join(journal_data))


def get_full_pathname(name):
    """
    het maken van de het volledige path met daarachter het bestand met daar weer achter .jrl (hier hadden we het OS voor nodig)
    :param name: de naam welke ingegeven is door de gebruiker
    :return: het volledige path met filenaam
    """
    # hier wordt het path gemaakt, de os.path.abspath geeft onze huidige werk directorie. hierachter komt de submap journals zodat deze allemaal in dezelfde map komen te staan. en daarin het journal.jrl
    filename = os.path.abspath(os.path.join('.', 'journals', name + '.jrl'))
    print('dir is het load bestand: {}'.format(filename))
    # hier wordt het volledige path met filenaam terug gegeven
    return filename


def add_entry(text, journal_data):
    """
    de list journal_data wordt hier uitgebreid met een nieuwe entry welke in text staat
    :param text: de nieuwe entry die moet worden toegevoegd
    :param journal_data: de list waar de text aan toegevoegd moet worden
    :return: niets
    """
    journal_data.append(text)

def main():
    print(__name__)

if __name__ == "__main__":
    main()