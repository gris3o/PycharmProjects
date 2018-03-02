import csv
import Header
import data_types
try: # we proberen statistics te importeren, werkt dit niet dan gaan we naar except waar we onze eigen standin importerten als statistics
    import statistics
except:
    import statistics_standin as statistics
import os


def main():
    Header.print_header(title='Real Estate Data Miner App', bar='=')
    filename = get_data_file() # maken het absolute path aan voor onze data.csv file
    data = load_file(filename) # laad de file in het geheugen als list. en pars de csv file
    query_data(data)


def get_data_file():
    base_folder = os.path.dirname(__file__) # hiermee zetten we in base_folder het absolute path waar we op dit moment onze applicatie hebben staan
    return os.path.join(base_folder, 'data', 'data.csv')


def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as fin: # open het bestand als fin
        reader = csv.DictReader(fin) # lezen de fin in als dicternairy waarbij we de bovenste regel gebruiken als namen voor de collumen
        purchases = [] # lege dictonairy aanmaken
        for row in reader:
            p = data_types.Purchase.create_from_dict(row) # door de static in data_types staat de layout van de dict vast
            purchases.append(p) # voegen de regel toe aan de dict purchases

        return purchases #geven de purchases dictonary terug als uitkomst van deze functie


def query_data(data):
    data.sort(key=lambda p: p.price) # sort edit de data zelf op zijn plaats, met een lambda kan je een een regel def maken, in dit geval p: p.price
    high_purchase = data[-1]
    print('The most expensive house is ${:,} with {} beds and {} baths'.format(
        high_purchase.price,
        high_purchase.beds,
        high_purchase.baths))
    low_purchase = data[0]
    print('The most expensive house is ${:,} with {} beds and {} baths'.format(
        low_purchase.price,
        low_purchase.beds,
        low_purchase.baths))

   prices = [
       p.price # projection of items van wat we willen gebruiken, in dit geval p.price de prijs
       for p in data # de dataset die we gaan processen
   ]
   ave_price = statistics.mean(prices) # omdat statistics alleen met getallen werkt maken we eerst een list met daarin de prijs
   print("the average home price is ${:,}".format(int(ave_price)))

    two_bed_homes = [
        p # projection of items welke een in de nieuwe list two_bed_homes wordt opgeslagen
        for p in data #de dataset die we gaan processen
        if p.beds == 2 # nu voegen we een extra test bij onze loop toe. we willen nu alleen de 2 bed apartementen
    ]
    ave_price = statistics.mean([p.price for p in two_bed_homes]) # we geven eerst de projection aan (hoe we de list gaan noemen), daarna geven we de source aan, waar het vandaan komt. en als laatste het filter, in dit geval two_bed_homes
    ave_baths = statistics.mean([p.baths for p in two_bed_homes]) # een list cpmprehension wordt aangegeven met een []
    ave_sqft = statistics.mean([p.sq__ft for p in two_bed_homes])
    print("the average 2-bedroom home is ${:,}, baths={}, sq ft={:,} ".format(int(ave_price), round(ave_baths, 1), round(ave_sqft, 1)))


#    prices = []
#    input_beds = int(input('hoeveel slaapkamers? '))
#    input_baths = int(input('hoeveel badkamers? '))
#    for pur in data:
#        if pur.beds == input_beds and pur.baths == input_baths:
#            prices.append(pur)

#    for pri in prices:
#        print('Straat naam is: {straat}{linesep}Verkocht voor: {prijs}{linesep}Aantal slaapkamers: {slaapkamer}{linesep}Aantal badkamers {badkamer}{linesep}{linesep}'.format(
#            straat=pri.street,
#            prijs=pri.price,
#            slaapkamer=pri.beds,
#            badkamer=pri.baths,
#            linesep=os.linesep))


if __name__ == '__main__':
    main()
