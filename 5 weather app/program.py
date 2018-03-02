import requests
import bs4
import collections
import os

# deze named tupil maken we aan zodat we op naam de gegevens overal kunnen opvragen.
WeatherReport = collections.namedtuple('WeatherReport', 'cond, temp, scale, loc')


# ik heb zelf het liefst in de main geen daadwerkelijke python code. ik wil hier eigenlijk alleen maar functies aanroepen, hierdoor zijn de gemaakte onderdelen het makkelijkste her te gebruiken in andere programma's
def main():
    # voor de header geven we de naam van de app mee en het teken dat de bovenste en onderste balk gaat maken.
    print_the_header(title='Weather APP', bar='*')
    # response_tekst op None zetten, zodat we daarna een while not loop in kunnen tot de response_tekst gevuld is
    response_tekst = None
    # while not loop. zolang response_tekst leeg is voeren we dit uit.
    while not response_tekst:
        # response_tekst van de website halen, bij een foutcode halen we een lege response_tekst en gaan we opnieuw door de loop
        response_tekst = get_html()
    # de html omzetten naar bs4 data zodat we daar de de benodigde gegevens uit kunnen halen
    report = get_weather_from_html(response_tekst)
    # de daadwerkelijke data printen. en aan de gebruiker vragen in welke format hij de temp wilt zien.
    print_data(report)


def print_the_header(title, width=None, bar=None):
    # met try zoeken we enentuele fouten
    try:
        # width wordt gemaakt vanuit het os. als deze door pycharm ofzo wordt gerund hebben we geen os en dus een foutmelding
        width = (os.get_terminal_size().columns if width is None else width)
    # als we een error krijgen omdat we de breedte niet kunnen bepalen. bijvoorbeeld doordat we vanuit pycharm runnen doen we het volgende.
    except OSError as e:
        print('oeps, bepaling van de terminal breedte wordt niet ondersteund: {}'.format(e))
        width = 80  # stupid terminal in PyCharm doesn't support this get_terminal_size() function :(
    # als de lengte van de title oneven is dan halen we 1 van de breedte af
    width -= len(title) % 2  # zorgen dat de naam in het midden staat ook bij oneven lengte
    # als we geen bar mee geven is de bar standaard '-' als we hem wel mee geven dan wordt het deze bar
    minus = ('-' if bar is None else bar)
    # print statment met daarin alle 4 de header regels, eerst de bar"minus" over de hele lengte
    # , daarna de linesep (door de os.linesep werkt dit op alle os systemen) daarna de "sep" om in het midden te zetten.
    # sep is ook de lengte - de lengte van de titel gedeelt door twee. daarna weer een enter "linesep" gevolgd door een bar en een enter
    print('{minus}{linesep}{sep}{title}{sep}{linesep}{minus}{linesep}'.format(
        sep=' ' * int((width - len(title)) / 2),
        title=title,
        minus=minus * width,
        linesep=os.linesep
    ))


def get_html():
    # url maken door de gebruiker land, staat, en stad op te vragen
    url_in_main = get_city_from_user()
    # doordat het downloaden van de data soms lang kan duren geef ik de melding dat de data gedownload wordt.
    print('please wait while we download the data')
    # de site daadwerkelijk opvragen
    response = requests.get(url_in_main)
    # controleren of de response code 200 is. nee dan geven we een lege return anders returnen we de verkregen html text data
    if response.status_code != 200:
        print("sorry the site can't find your city")
        return None
    else:
        return response.text



def get_city_from_user():
    # omdat de zipcode alleen werkt in de us heb ik de url aangepast en vraag ik eerst het land en daarna de stad, als er voor de us gekozen wordt moet in de url de staat nog mee gegeven worden.
    land = ''
    # om te zorgen dat we maar 2 letters als land invoeren doen we de onderstaande while loop
    while len(land) != 2:
        land = input('in witch country do you want to know the weather: (use the 2 letter code)')
    # als het land de us is, dan gebruikt de site ook de staat, dus die hebben we dan nodig
    if land.lower() == 'us':
        # opvragen van de state
        state = input("for us city's please give the state: (use the 2 letter code)")
        # de state aanpassen met de / er voor zodat we deze / alleen toevoegen als we een state hebben
        state = '/{}'.format(state)
    # als we geen state hebben zorgen we dat deze zeker leeg is
    else:
        state = ''
    # nu vragen we de stad waar we het weer willen weten
    stad = input('please give the city name: ')
    # omdat de site geen spaties gebruikt. maar sommige steden wel een spatie hebben vervangen we de spatie met een "-" zodat we ons aan de url houden
    stad = '/{}'.format(stad.replace(' ', '-'))
    # hier wordt de url samengevoegd.
    url = 'https://www.wunderground.com/weather/{}{}{}'.format(land, state, stad)
    return url


def get_html_from_web(url):
    # binnen halen van de website
    response = requests.get(url)
    # controleren of we een foutmelding krijgen of niet (goed inladen van een website geeft de 200 code)
    if response.status_code == int('200'):
        return response.text
    else:
        print('sorry we could nog find your input, exiting')
        exit()


def get_weather_from_html(html):
    # de html omzetten in soup zodat we er doorheen kunnen zoeken
    soup = bs4.BeautifulSoup(html, 'html.parser')
    # de locatie uit de html halen en wegschrijven in loc
    loc = soup.find(class_='region-content-header').find('h1').get_text()
    # de conditie uit de html_soup halen en wegschrijven in condition
    condition = soup.find(class_='condition-icon').find('p').get_text()
    # temp uit de html halen en wegschrijven
    temp = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text()
    # temp type uit de text halen en wegschrijven
    temp_scale = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text()
    # de functie cleanup aanroepen om de text schoon te maken van <enters> en spaties
    loc = cleanup_text(loc)
    # de funcite find city aanroepen om eventuele <enters> te verwijderen
    loc = find_city_from_location(loc)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    temp_scale = cleanup_text(temp_scale)
    # het maken van een named_tupel genaamd report met daarin alle waardes om die te kunnen returnen
    report = WeatherReport(cond=condition, temp=temp, scale=temp_scale, loc=loc)
    return report


def find_city_from_location(loc: str):
    # alle <enters> verwijderen uit het locatie gedeelte
    parts = loc.split('\n')
    return parts[0].strip()


def cleanup_text(text: str):
    # kijken of text leeg is. zo ja niets doen en lege tekst terug geven naar waar hij aangeroepen werd
    if not text:
        return text
    # als er iets in text staat alle spaties verwijderen en text terug geven
    text = text.strip()
    return text


def print_data(report):
    # vragen of we de temp in graden Celsium of farenheid willen zien
    temp_input = input('would u like the temp in F our C? ')
    # de input hoofdlettersmaken en eventueele spaties enz verwijderen
    temp_input = temp_input.upper().strip()
    # als de waardes al in de goede mode staan, print dan de uitkomst
    print_temp = report.temp
    if temp_input == 'F' and report.scale == 'C':
        # maak van de celcius farenheid
        # haal uit de tupil de temp om deze te bewerken en sla op als int
        report_temp = int(report.temp)
        # rekenen en met behulp van round ronden we af. door de %. geven we het aantal getallen achter de comma (1f = 1float) en met de laatste , geven we af waar we op willen afronden (aantal decimalen)
        print_temp = report_temp * 1.8 + 32

    elif temp_input == 'C' and report.scale == 'F':
        report_temp = int(report.temp)
        print_temp = (report_temp - 32) / 1.8

    print('The temp in {location} is {degrees:.1f}{unit} and {weather_condition}'.format(
        location=report.loc,
        degrees=print_temp,
        unit=temp_input,
        weather_condition=report.cond
    ))


if __name__ == '__main__':
    main()
