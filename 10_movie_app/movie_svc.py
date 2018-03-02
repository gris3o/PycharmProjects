import requests
import collections

MoviesResult = collections.namedtuple(
    'MovieResult',
    "imdb_code,title,duration,director,year,rating,imdb_score,keywords,genres")


def find_movies(search_text):

    if not search_text or not search_text.strip():
        raise ValueError ("Search text is required") # als er geen tekst is ingegeven of een spatie wordt deze valueError gezet. en aan de try terug gegeven waardoor de exception wordt aangeroepen.
    url = 'http://movie_service.talkpython.fm/api/search/{}'.format(search_text) # voeg de url samen van de hardcoded en de input.

    resp = requests.get(url) # download de url die hier boven is gemaakt van de hardcoded en de input
    resp.raise_for_status() # als er geen goede htlm status code terug komt wordt hier een exception geraised.

    movies_data = resp.json() # omdat python vaak gebruik maakt van json api's is er een module die de data meteen in een dictonairy kan zetten.
    movies_list = movies_data.get('hits') # hier wordt uit de movie_data de lijst met hit's gehaald. (gefilterd op hits)

    movies = [
        MoviesResult(**md) # met de ** halen we de namen uit de dictonarie en gebruiken die als key word arguments. we gebruiken de namen van de dictonairy velden dus als namen voor onze named tuple
        for md in movies_list # nu vullen we onze namedtuple.
    ] # nu maken we een list waar we onze hits in zetten. (dit is de mooist manier vind ik) we zetten de opdracht direct wanneer we de list aanmaken, andere manieren staan hieronder uit gehased)

    movies.sort(key=lambda m: -m.year) # nu sorteren we op jaar. de nieuwste bovenaan, door de - geven aan hoogste eerst dit werkt met cijvers.

    return movies



# movies = []
# for md in movies_list:
#     m = MoviesResult(
#         imdb_code=md.get('imdb_code'),
#         title=md.get('title'),
#         duration=md.get('duration'),
#         director=md.get('director'),
#         year=md.get('year', 0),
#         rating=md.get('rating', 0),
#         imdb_score=md.get('imdb_score', 0.0),
#         keywords=md.get('keywords'),
#         genres=md.get('genres'),
#     )
#     movies.append(m)

# movies = []
# for md in movies_list:
#     m = MoviesResult(**md)
#     movies.append(m)






