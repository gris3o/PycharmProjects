import os
import requests
import shutil


def get_cat(folder, name):
    # de url waarvandaan we downloaden
    url = 'http://consuming-python-services-api.azurewebsites.net/cats/random'
    # de data downloaden via de functie
    data = get_data_from_url(url)
    # de gedownloade data saven als plaatje
    save_image(folder, name, data)

def get_data_from_url(url):
    # de response downloaden van de url (het plaatje) omdat we met een raw-stream werken in response moeten we de request een stream=true mee geven
    response = requests.get(url, stream=True)
    # de ruwe data die we hebben gedownload returnen
    return response.raw

def save_image(folder, name, data):
    # de filenaam aanmaken, door het os.path samen te voegen met de folder en daar dan het bestand in maken met de extentie .jpg
    file_name = os.path.join(folder,'{}.jpg'.format(name))
    # het bestand openen als fout (file output) met write en binairy rechten
    with open(file_name, 'wb') as fout:
        # de data wegschrijven van de data naar de fout (file output) met behulp van de shell utility en copyfileobject. de fout wordt hierboven weer weggeschreven als de daatwerkelijke file
        shutil.copyfileobj(data, fout)