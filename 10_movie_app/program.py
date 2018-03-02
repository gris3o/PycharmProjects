import Header
import movie_svc
import requests.exceptions

def main():
    Header.print_header(title='movie search app', bar='=')
    search_event_loop()



def search_event_loop():
    search = 'ONCE_THROUGH_LOOP'

    while search != 'x': # zolang we geen x ingeven blijft de app draaien
        try: # door de try proberen we het, gaat het niet dat gaan we naar exception. er kunnen zelfs specifieke exceptions aangeroepen worden. en daarna gaan we terug de while loop in. ipv dat de app crashed
            search = input("What movie do you want to search for? (x to exit): ")
            if search != 'x':
                results = movie_svc.find_movies(search)
                print("Found {} movies results".format(len(results)))
                for r in results:
                    print("{} -- {}".format(r.year, r.title))
                print()
        except ValueError: # deze exception wordt aangeroepen in de movie_svc routine als er geen tekst is ingegeven.
            print("Error: Search text is required")
        except requests.exceptions.ConnectionError: # deze exception wordt gezet als er netwerk problemen zijn. we controleren of de type of exception
            print("Error: Your network is down")
        except Exception as x: # nu wordt de rede van de exception mee gegeven als x, en deze wordt vervolgens geprint is de onderstaande print opdracht.
            print("Unexpected error! Details: {}".format(x))
    print('exiting...')



if __name__ == '__main__':
    main()
