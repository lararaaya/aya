import requests
from bs4 import BeautifulSoup
def recuperer_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return BeautifulSoup(response.text, "html.parser")
    else:
        print("erreur :" , response.status_code)
        return None
def extraire_titre(soup):
    titre = soup.find("h1")
    return titre.get_text(strip=True) if titre else None
def extraire_text(soup):
    contenu = {}
    titre_actuel = "Introduction"
    contenu[titre_actuel] = []
    for element in soup.select("#mw-content-text h2, #mw-content text h3 , #mw-content text p"):
        if element.name in ["h2" , "h3"]:
            titre_actuel = element.get_text(" ", strip=True)
            contenu[titre_actuel] = []
        elif element.name == "p":
            text = element.get_text(" ", strip=True)
            if text:
                contenu[titre_actuel].append(text)
    return contenu
def extraire_liens(soup):
    liens = []
    for a in soup.select("a[href]"):
        href = a["href"]  
        if href.startswith("/wiki/") and not href.startswith("/wiki/special"):
            lien = "https://fr.wikipedia.org" +href
            if lien not in liens:
                liens.append(lien)
    return liens
def scraper_wikipedia(url):
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        response = requests.get(url,headers=headers)
        if response.status_code !=200:
            print("Erreur :" , response.status_code)
            return None
        soup = BeautifulSoup(response.text, "html.parser")
        titre = extraire_titre(soup)
        text = extraire_text(soup)
        liens = extraire_liens(soup)
        return{
        "titre": titre,
        "texte": text,
        "liens": liens,
    } 

url = "https://fr.wikipedia.org/wiki/Intelligence_artificielle"
resultat = scraper_wikipedia(url)
print("TITRE :")
print(resultat["titre"])
print("\nTEXTE :")
for titre, paragraphes in resultat["texte"].items():
    print("---", titre, "---")
    for paragraphe in paragraphes:
        print(paragraphe)    
print("\nLIENS :")
for lien in resultat["liens"]:
    print(lien)               
