import os

def print_header(title, bar=None, width=None):
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        width = (os.get_terminal_size().columns if width is None else width)
    except OSError as e:
        print('oeps, bepaling van de terminal breedte wordt niet ondersteund: {}'.format(e))
        width = 80  # stupid terminal in PyCharm doesn't support this get_terminal_size() function :(
    width -= len(title) % 2
    minus = ('-' if bar is None else bar)
    print('{minus}{linesep}{sep}{title}{sep}{linesep}{minus}{linesep}'.format(
        sep=' ' * int((width - len(title)) / 2),
        title=title,
        minus=minus * width,
        linesep=os.linesep
    ))