import re
import base64
import requests

link = input("Link do razreda: ") # važno je da link završava sa znakom "/", primjer: https://www.matura.hr/maturanti/2010_2011/zadar/pomorska-skola-zadar/4BN/
print()
session = requests.Session()
response = requests.get(link) # šaljemo GET Request do danog linka
osobe = re.findall('<img src="(.*?) class="matura-maturant-image"', response.text) # koristimo regex kako bi pronašli svaki link do slike
for svakaOsoba in osobe: # petlja jer postoji više nego jedan učenik (nevjerojatno)
    osoba = str(svakaOsoba).split("maturant.php?id=")[1].replace('"', '') # split-amo string tako da nam samo ostane base64 encoded string i maknemo znak '"'
    osobaDecoded = base64.b64decode(osoba) # decode-amo string
    linkVazno = link.split("https://www.matura.hr/maturanti/")[1] # ostavljamo važni dio linka
    # s obzirom da postoje dvije vrste linka, imamo try statement
    try:
        osobaIme = str(osobaDecoded, "utf-8").split("slike/generacija")[1].split(linkVazno + "1/")[1].replace(".jpg", "").replace("_", " ") # prvi slučaj (spaghetti code)
    except:
        osobaIme = str(osobaDecoded, "utf-8").split("slike/generacija")[1].split(linkVazno + "bg/")[1].replace(".jpg", "").replace("_", " ") # drugi slučaj (spaghetti code)
    linkSlike = "https://www.matura.hr/img/" + str(osobaDecoded, "utf-8") # varijabla za link do slike
    print("Link do slike: " + linkSlike + "\nIme: " + osobaIme) # printamo rezultat