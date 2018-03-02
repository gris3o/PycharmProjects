import os
import collections
import Header

SearchResult = collections.namedtuple('SearchReult',
                                      'file, line, text') # aanmaken van een named tuple


def main():
    Header.print_header(title='File Search App', bar='=')
    folder = get_folder_from_user()
    if not folder: # controleren of er iets is ingegeven
        print("sorry we can't search that location ")
        return
    text = get_search_text_from_user()
    if not text: # controleren of er iets ingegeven is
        print("we can't search for nothing")
        return
    matches = search_folders(folder, text)
    hit_count = 0
    for m in matches: # hiermee printen we de uitkomst van onze zoek opdrach
        hit_count += 1 # het aantal gevonden keren van de tekst bijhouden
        Header.print_header(title=('file: {file}{linesep}match: {match}{linesep}found on line: {line}'.format(
            file=m.file,
            line=m.line,
            match=m.text.strip(),
            linesep=os.linesep)), bar='*') # de gevonden hits
    Header.print_header(title=("total number of hit's {}".format(hit_count)), bar="-") # printen van het aantal gevonden keren van de zoekopdracht

def get_folder_from_user():
    folder = input('What folder fo you want to search? ')
    print(folder)
    if not folder or not folder.strip(): # controleren of er iets ingegeven is of een spatie
        return None
    if not os.path.isdir(folder): # als het geen folder is maar wel bestaat (bijvoorbeeld een bestand willen we ook een foutmelding genereren
        return None
    return os.path.abspath(folder) # geef het absolute path terug


def get_search_text_from_user():
    text = input('What are you searching for [single phrases only]?')
    return text.lower() # de zoektekst terug geven als kleine letters


def search_folders(folder, text):
    items = os.listdir(folder) # met listdir halen we alle bestand en folder namen uit de folder
    for item in items:
        full_item = os.path.join(folder, item) # we maken er hier het absolute path van
        if os.path.isdir(full_item): # controleren of het een bestand of een map is.
            yield from search_folders(full_item, text) # als het een map is roepen we de search_folder aan tot deze klaar is en gaan we hier verder, hiervoor geven we de full_item terug ipv de folder. waarbij de full_item nu het nieuwe absulute pad is met de een laag diepere map.

        else:
            yield from search_file(full_item, text) # als het een bestand is dan roepen we de search_file aan tot deze klaar is en gaan we hier verder


def search_file(filename, rearch_text):
    with open(filename, 'r', encoding='utf-8') as fin: # open de filename (dat is het absolute path) als readonly en als text (utf-8)
        line_num = 0 # we zetten de regel teller op 0 zodat we straks kunnen aangeven op welke lijn het woord staat
        for line in fin:
            line_num += 1 # dit doen we voor elke regel dus we tellen hier het aantal regels
            if line.lower().find(rearch_text) >= 0: # we maken er eerst van de regel in de tekst lage karaters en dan zoeken we met find of de rearch_text er in staat
                m = SearchResult(line=line_num, file=filename, text=line) # nu geven we de gevonden parameters terug
                yield m # we blijven net zolang door het bestand gaan tot er geen regels meer zijn om door te zoeken


if __name__ == '__main__':
    main()
