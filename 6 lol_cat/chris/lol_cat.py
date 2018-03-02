import os
import platform
import cat_service
import subprocess
import argparse

def main(kat_map, kat_aantal):
    print_header()
    folder = get_or_create_output_folder(kat_map)
    print('Found or created folder: ' + folder)
    download_cats(folder, kat_aantal)
    display_cats(folder)



def print_header():
    print('--------------------------')
    print('       CAT FACTORY        ')
    print('--------------------------')
    print()


def get_or_create_output_folder(folder):
    base_folder = os.path.abspath(os.path.dirname(__file__))
    full_path = os.path.join(base_folder, folder)
    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('Creating new directory at {}'.format(full_path))
        os.mkdir(full_path)

    return full_path


def download_cats(folder, cat_count):
    print('Contacting server to download cats...')
    for i in range(1, cat_count + 1):
        name = 'lolcat_{}'.format(i)
        print('Downloading cat ' + name)
        cat_service.get_cat(folder, name)

    print("Done. ")


def display_cats(folder):
    print('Displaying cats in OS window')
    if platform.system() == 'Darwin':
        subprocess.call(['open', folder])
    if platform.system() == 'Windows':
            subprocess.call(['explorer', folder])
    elif platform.system() == 'Linux':
        subprocess.call(['xdg-open', folder])
    else:
        print("We don't support your OS: " + platform.system())


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mapnaam", help="Vul hier de naam van de doelsmap in")
    parser.add_argument("-a", "--aantal", help="Vul hier het gewenste aantal lolcats in", type=int)
    args = parser.parse_args()
    doelmap = "lolcatzondernaam" if not args.mapnaam else args.mapnaam
    aantal = 8 if not args.aantal else args.aantal
    main(kat_map=doelmap, kat_aantal=aantal)

