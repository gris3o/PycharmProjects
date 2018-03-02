# eerst importeren we het programma journal.py in dit subprogramma wordt alle I/O geregeld in het programma.py wordt alleen de UI geregeld
import journal
import datetime


# wederom staat de main bovenaan zodat we goed kunnen zien hoe het programma loopt
def main():
    # de header printen
    print_header()
    # de daadwerkelijke loop uitvoeren waar het programma uit bestaat
    run_event_loop()


def print_header():
    """
    print de header
    :return:
    """
    print('=======================================================')
    print('               JOURNAL APP')
    print('=======================================================')
    print('')


def run_event_loop():
    """
    hier wordt aan de gebruiker gevraagd wat hij wilt doen, dag boek bekijken of juist nieuwe items toevoegen
    :return:
    """
    # in de while loop verder op wordt er gekeken naar de variable cmd. deze moet eerst gedefinieerd worden
    cmd = 'EMPTY'
    # we zetten nu de journal name op "None" dan is hij leeg en kunnen we straks kijken of hij leeg is.
    # is hij leeg dan vragen we de naam op. dit doen we om te zorgen dat we in de while loop kunnen wisselen van gebruiker
    journal_name = None
    print('What do you want to do with your journal?')
    # onderstaande while loop wordt uitgevoerd zolang er geen "x" wordt ingegeven of direct op enter wordt gedrukt.
    while cmd != 'x' and cmd:
        # zolang journal_name leeg is wordt onderstaande if uitgevoerd, we vragen hier de gebruikersnaam op (dit gebeurt als we het script de eerst keer draaien, of van gebruiker wisselen dan gooien we journal_name namelijk leeg
        if not journal_name:
            # dit heb ik gedaan zodat er meerdere journals gemaakt worden voor meerder mensen
            journal_name = input('Please give your yournal name: ')
            # hier wordt de load functie aangeroepen in het journal.py programma, de return van deze functie wordt opgeslagen in journal_data
            journal_data = journal.load(journal_name)

        # vraag aan de gebruiker wat hij wilt doen en sla dit op in "cmd"
        cmd = input('[L]ist entries, [A]dd entry, [C]hange journal, [x] our <enter> to exit: ')
        # om te zorgen dat cmd altijd lowercase is en er geen eventuele spaties voor kunnen staan gebruiken we .lower() "om er kleine letters van te maken en .strip() om alleen de ingevoerde letter te gebruiken
        cmd = cmd.lower().strip()
        # als er een "L" is ingevoerd voer het onderstaande uit
        if cmd == 'l':
            # de sub functie list entry wordt aangeroepen en de data uit journal_data wordt mee gegevens als variable
            list_entries(journal_data)
        # als er een "A" is ingevoerd voer dan onderstaande uit:
        elif cmd == 'a':
            # de functie add_entry wordt nu aangeroepen en de data uit journal_data wordt meegegeven als variable
            add_entry(journal_data)
        # als er een "c" wordt ingegeven wordt onderstaande uitgevoerd:
        elif cmd == 'c':
            # eerst wordt de functie save in het journal.py bestand uitgevoerd, de variablen journal_name en Journal_data worden mee gegeven
            journal.save(journal_name, journal_data)
            # nu zetten we de variable journal_name terug naar None (leeg) zodat in de eerste if statement in de while loop deze weer gevuld wordt en we dan met die gebruiker verder gaan in de while loop.
            journal_name = None
        # als er een teken wordt ingevoerd welke niet hierboven wordt beschreven ( x, l, a, en c) wordt er aangegeven dat dit teken niet bekend is
        elif cmd != 'x' and cmd:
            # hier wordt daadwerkelijk geprint dat we het teken niet herkennen en welk teken dat is
            print("sorry, we don't understand '{}'".format(cmd))
    # hier wordt de goodbye message geprint
    print('Done, goodbye')
    # hier wordt de functie save in het journal.py bestand uitgevoerd, de variablen journal_name en Journal_data worden mee gegeven om de data op te slaan
    journal.save(journal_name, journal_data)


def list_entries(data):
    """
    in deze functie worden de entrys welke in het journal staan geprint
    :param data: het daadwerkelijke journal
    :return: none
    """
    # print wat er gaat gebeuren
    print("Your journal entry's")
    # hier worden er gezorgd dat de enties worden omgedraaid. nieuwste eerst.
    entries = reversed(data)
    # door het enumerate commando krijgen de entrys in de list een volgnummer, dit nummer slaan we op in idx "index" voor elke entry wordt het onderstaande uitgevoerd
    for idx, entry in enumerate(entries):
        # hier worden alle entries daadwerkelijk geprint. doordat python met 0 begint met tellen en wij als mensen met 1 beginnen geven we de "+ 1" zodat python ook met 1 lijkt te beginnen
        print('* [{}] {}'.format(idx + 1, entry))


def add_entry(data):
    """
    hier wordt data opgevraagd om toe te voegen aan de list
    :param data: de huidige journal
    :return:
    """
    # print wat we gaan doen, en wat we willen, nieuwe input opvragen
    text_zonder_datum = input('type your entry, <enter> to exit: ')
    # de datum van vandaag opvragen en deze als string opslaan in datum_nu
    datum_nu = str(datetime.date.today())
    # de text die we gaan opslaan in de list met daarbij de datum wordt hier gemaakt
    text = '{datum}: {text}'.format(datum=datum_nu, text=text_zonder_datum)
    # de daadwerkelijke append vind plaats in het journal.py programma wat hier wordt aangeroepen en de "text" welke is ingoerd wordt mee gegeven net als de "data" wat de huidige joural inhoud is
    journal.add_entry(text, data)


"""
hier wordt de main functie op de nette manier aangeroepen. 
eerst wordt er gekeken of dit programma wordt aangeroepen door de gebruiker of door een ander programma.
wordt er door een ander programma een functie uit dit programma opgroepen dan staat in de __name__ de naam van de functie die deze functie oproept.
doordat python het hele programma inleest om zeker te zijn dat alle eventuele functies kunnen worden uitgevoerd komt python de main() tegen en gaat dat het hele programma uitvoeren. 
ook al willen we alleen maar die ene functie.
nu controleren we of de waarde in __name__ gelijk is aan __main__ (de waarde die __name__ krijgt als dit programma door de gebruiker wordt uitgevoerd) als dit zo is. dan pas voeren we main() uit
"""
if __name__ == '__main__':
    main()
