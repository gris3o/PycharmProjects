import os
import cat_service
import subprocess
import platform
import argparse

def main(kat_map, kat_aantal):
    # print the header
    print_header()
    # get our create output folder
    folder = get_or_create_output_folder(kat_map)
    print('Found or created folder: {}'.format(folder))
    # download images
    download_cats(folder, kat_aantal)
    # open browser op het os systeem om de plaatjes te laten zien
    display_cats(folder)



def print_header():
    print('----------------------------------------------')
    print('               CAT FACTORY                    ')
    print('----------------------------------------------')
    print('')


def get_or_create_output_folder(folder):
    # De folder naam maken door door te kijken waar het programma vanuit uitgevoerd wordt zodat hier een subfolder wordt gemaakt voor onze cat plaatjes
    base_folder = os.path.abspath(os.path.dirname(__file__))
    # hier worden het full path en de naam in cat_folder samen gevoegd tot een path
    full_path = os.path.join(base_folder, folder)
    # als het path nog niet bestaat maken we hem aan, of als er al een bestand is dat deze naam heeft maken we hem aan
    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('Creating new directory at: {}'.format(full_path))
        # het daarwerkelijk aanmaken van de directorie
        os.mkdir(full_path)
    return full_path


def download_cats(folder, cat_count):
    print('Contacting server to download cats.......')
    # aangeven hoeveel plaatjes we willen downloaden
    # for het aantal keer opgegeven in cat_count voeren we onderstaande uit.
    for i in range(1, cat_count + 1):
        # maken de naam aan, plus de hoeveelste keer we hem uitvoeren
        name = 'lolcat_{}'.format(i)
        # printen dat we het bestand downloaden
        print('downloading {}'.format(name))
        # roepen de funtie aan waaruit we daadwerkelijk downloaden (in het cat services script)
        cat_service.get_cat(folder, name)
    print('done')


def display_cats(folder):
    # open folder voor het os systeem waar het script op draait
    print('Displaying cats is OS windows.')
    # als het mac is
    if platform.system() == 'Darwin':
        # met subprocess.call roepen we een programma aan in het os in dit geval open folder
        subprocess.call(['open', folder])
    # als het windows is
    elif platform.system() == 'Windows':
        # hier openen we explorer met als path de folder waar de katten zijn gedownload
        subprocess.call(['explorer', folder])
    # als het Linux is
    elif platform.system() == 'Linux':
        # hier openen we de map als nieuwe window in linux
        subprocess.call(['xdg-open', folder])
    else:
        print("We don't support your os: " + platform.system())




if __name__ == '__main__':
    # door de argparser kunnen we argumenten mee geven als we het programma runnen vanaf de command promt en eventuele help toegevoegd.
    parser = argparse.ArgumentParser()
    # het argument --mapnaam (afgekort -m) met meteen de help aanvulling voor de help file.
    # de -- betekend dat het een optioneel argument is.
    parser.add_argument("-m", "--mapnaam", help="Vul hier de naam van de doelsmap in")
    # het argument --aantal (afgekort -a) met meteen de aanvulling van de help file, dit argument is een int, dus we zetten de type hier ook meteen op.
    parser.add_argument("-a", "--aantal", help="Vul hier het gewenste aantal lolcats in", type=int)
    # hiermee slaan we de argumenten op in de var args
    args = parser.parse_args()
    # als er geen doelmap wordt opgegeven is de default lolcatzondermap, anders wordt de --mapnaam mee gegeven als doelmap
    doelmap = "lolcatzondermap" if not args.mapnaam else args.mapnaam
    # als er geen aantal wordt meegegeven worden er standaard 8 plaatsjes gedownload, als er wel een --aantal wordt mee gegeven wordt dit aantal mee gegeven
    aantal = 8 if not args.aantal else args.aantal
    # het aanroepen van de main functie met de named arguments.
    main(kat_map=doelmap, kat_aantal=aantal)
