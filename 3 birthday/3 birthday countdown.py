import datetime


# ik heb de main boven aan gezet zodat het programma overzichtelijker wordt.

def main():
    # om de header te printen
    print_header()
    # deze functie vraagt de verjaardag van de gebruiker en bewaart deze in "bday"
    bday = get_birthday_from_user()
    # hier wordt de datum van vandaag opgeslagen in "today"
    today = datetime.date.today()
    # in "number_of_day's wordt de uitkomst van de functie "compute_days_between_dates bewaard. deze suroutine krijgt de variable mee welke in "bday" en "today" zijn opgeslagen
    # we geven de target variable ook mee op deze manier weten we zeker dat ze op de goede locatie worden ingeladen. zo hoeft de volgorde niet overeen te komen
    number_of_days = compute_days_between_dates(orignal_date=bday, targer_date=today)
    # print de uitkomst van de vergelijking, deze uitkomst wordt mee gegeven als uitkomst van bovenstaande functie als "number_of_days"
    print_birtday_information(number_of_days)


def print_header():
    '''
    header printen
    :return:
    '''
    print('=======================================================')
    print('                Birthday countdown')
    print('=======================================================')
    print('')


def get_birthday_from_user():
    '''
    verjaardag opvragen, door de verschillende notaties in datum's doen we dit in drie stappen.
    :return: birthday
    '''
    print('when were you born?')
    # vraagt het jaar aan de gebruiker en maakt van deze input meteen een interger omdat datum's uit integers bestaan en niet uit variablen
    year = int(input('Year [YYYY]: '))
    # vraagt  de maand aan de gebruiker en maakt van deze input meteen een interger omdat datum's uit integers bestaan en niet uit variablen
    month = int(input('Month [MM]: '))
    # vraagt  de dag aan de gebruiker en maakt van deze input meteen een interger omdat datum's uit integers bestaan en niet uit variablen
    day = int(input('Day [DD]: '))
    # hier worden de ingegeven waardes samen gevoegd in "birthday" en wordt er een datum van gemaakt doormiddel van het datetime.date gedeelte
    birthday = datetime.date(year, month, day)
    # mbv het return commando wordt de waarde van de daarachter genoemde varialbe als uikomst van de functie gegeven naar waar hij werd aangeroepen. In dit geval naar main waar deze weer wordt opgeslagen in bday
    return birthday


def compute_days_between_dates(orignal_date, targer_date):
    '''
    dagen tussen vandaag en de verjaardag berekenen. we krijgen van uit de main functie nu de huidige datum en de verjaardag (let op het maakt niet uit hoe deze variable heten in het aanroepen en de daadwerkelijke functie. ze worden op volgorde gevuld)
    :param :orignal_date, targer_date
    :return: dt.days
    '''
    # hier wordt het jaartal vervangen door het huidige jaar, zodat we het aantal dagen tussen nu en de verjaardag kunnen bepalen.
    this_year = datetime.date(targer_date.year, orignal_date.month, orignal_date.day)
    # hier wordt het verschil tussen vandaag en de verjaardag berekend en opgeslagen in "dt"
    dt = this_year - targer_date
    # de functie wordt nu afgesloten en de variable achter return wordt terug gegeven als uitkomst van deze funstie aan main, letop door de dt.days, en dan het day's gedeelte wordt er gekeken naar het aantal dagen, hier kunnen ook andere waardes worden gegeven zoals maanden
    return dt.days


def print_birtday_information(days):
    '''
    hier wordt er gekeken of je in de toekomst jarig bent of dat je al jarig bent geweest
    :param : days
    :return:
    '''
    # als de waarde days kleiner is als 0 (dus negatief) dan ben je dit jaar al jarig geweest dan wordt onderstaande geprint.
    if days < 0:
        # door de .format(-days) wordt het negatieve getal in days omgezet in een positief getal "-" + "-" is immers "+"
        print('You had your birthday {} days ago this year.'.format(-days))
    # als de waarde days groter is al 0 dan is je verjaardag in de toekomst. nu wordt er geprint hoeveel dagen het nog is tot je verjaardag
    elif days > 0:
        print('Your birthday is in {} days.'.format(days))
    # als je days niet groter of kleiner is als 0 dan moet het wel 0 zijn, en ben je vandaag jarig. gefeliciteerd
    else:
        print('Happy birthday!')


'''
 nadat eerst het hele programma is ingelezen (python leest van boven naar beneden) wordt helemaal onder de functie main aangeroepen. 
 Dit doen we helemaal onderaan zodat we zeker weten dat alle sub functies bekend zijn bij python.
 Dit is niet de mooiste manier van aanroepen maar dit wordt in het volgende programma netter gedaan en uitgelegd.
'''
main()
