#! /usr/bin/env python

from datetime import date

# een functie om het kortst herhalende patroon te vinden in een reeks

def find_repeat(reeks):

  # we zoeken het kortste herhalende patroon, dat begint op positie 0 in de reeks
  # dat kan dus niet langer zijn dan de helft van de array lengte
  # we proberen alle patroon lengtes van 1 tot de helft vd lengte (ga nooit verder dan halverwege)
  # pat_len is de te-bewijzen patroon lengte

  for pat_len in range(1, int(len(reeks)/2 +1)):
    
    # als het patroon een lengte pat_len heeft geldt:  reeks[x] == reeks[x+pat_len] for all x < pat_len

    found_pat=True # we beginnen met de veronderstelling dat er een patroon is...

    for x in range(0, pat_len): # for all x < pat_len
      if reeks[x] != reeks [x+pat_len]: # != betekent is-ongelijk
        found_pat=False # ... totdat het tegendeel bewezen wordt
        break # als op positie x het patroon afwijk, breken we uit de for loop (scheelt tijd)
    
    # als found_pat nog steeds True is na pat_len vergelijkingen, is er dus geen afwijkende waarde gevonden
    # en herhaalt het patroon zich TEN MINSTE 1x in de gegeven reeks

    # eigenlijk moet je bij een vermeende match ook nog kijken of het patroon zicht voortzet
    # want nu zalin [1,2,1,2,3,4] 1,2 als herhalend patroon worden gezien
    # de if in de for loop zou dus eigenlijk ook moeten controleren of na 1 herhaling niet van het patroon
    # wordt afgeweken....


    if found_pat:
      print('[Kandidaat] Patroon gevonden, lengte is: ', pat_len)

      # toch even kijken of het blijft herhalen

      max_pats = int (len(reeks)/pat_len) # hoevaak past het patroon maximaal in de reeks

      # r is de vermenigvuldiging, r=1 hebben we hierboven al getest, 
      # nu voor r=2 en verder moet het patroon blijven herhalen OF we zijn aan het eind van de input
      
      for r in range(2, max_pats + 1): 
        for x in range(0, pat_len): # for all x < pat_len

          if x+r*pat_len >= len(reeks):  # maar we moeten wel binnen de reeks blijven kijken!
            break # einde van de input is geen reden de kandidaat te verwepen!

          if reeks[x] != reeks [x+r*pat_len]: # != betekent is-ongelijk
            found_pat=False # ... totdat het tegendeel bewezen wordt
            break # als op positie x het patroon afwijk, breken we uit de for loop (scheelt tijd)

      # als na bovenstaande loops found_pat nog steeds True is, 
      # hebben we een blijvend repeterend patroon in de reeks!

      if found_pat:
        print('Kandidaat patroon blijft herhalen')
      else:
        print('Kandidaat valt toch af')
      
## main code

# enkele test

find_repeat([1,2,1,2,2,3]) # na 1 herhaling niet langer
find_repeat([1,2,1,2,1,3]) # laatse positie valt uit de toon
find_repeat([1,2,1,2,1,2,3]) # na 3 perfecte herhalingen, laatste positie verschilt
find_repeat([1,2,1,2,1,2,1]) # na 3 perfecte herhalingen, laatste positie klopt 

dag_van_de_maand = 13
startjaar=1400
dagen = [] # maakt een leeg array genaamd dagen

# range(van, tot) --> let op, niet (van, totenmet)!!
# vul het dagen array met de weekdag voor de 13e van iedere maand voor een periode van 800 jaar

for jaar in range(0, 800):
  for maand in range (1, 13):
    # voeg de weekdag toe aan het array dagen
    dagen.append ( date(startjaar + jaar , maand, dag_van_de_maand).weekday() )

# bepaal de (kortste) lengte van een herhalend patroon

find_repeat(dagen)
