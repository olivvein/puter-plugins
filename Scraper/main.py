import requests
from bs4 import BeautifulSoup
import urllib.parse

# Fonction pour scraper le site de Boulanger pour obtenir le prix d'un produit
def scrape_boulanger(query):
    # Encode la requete
    query = urllib.parse.quote_plus(query)

    # Trouve l'url du website qua,d tu fais une recherche sur le site
    #construis l'url avec la requete
    url = f'https://www.boulanger.com/resultats?tr={query}'
    print(url)

    # Send request to the website
    
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, allow_redirects=True)

    # Verifie que la requete fonctionne
    if response.status_code == 200:  #code 200 = OK
        # Parse le contenu de la page avec BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        #Dans chrome, click droit sur le prix et inspecter pour trouver le selecteur CSS
        #price selector:#product-list > ul > li:nth-child(1) > article > div.product-list__product-area-3.g-col-5.g-col-sm-7.g-col-md-4.g-start-md-9.g-col-lg-3.g-start-lg-7.g-col-xl-3.g-start-xl-7 > div.price.price--medium > p
        #ca signifie dans le div #product-list, on veut le premier ul, puis le premier li, puis le premier article, puis le premier div, puis le premier div, puis le premier p
        priceData=soup.select_one('#product-list > ul > li:nth-child(1) > article > div.product-list__product-area-3.g-col-5.g-col-sm-7.g-col-md-4.g-start-md-9.g-col-lg-3.g-start-lg-7.g-col-xl-3.g-start-xl-7 > div.price.price--medium > p')
        print(priceData.text)
    else:
        print(f'Failed to retrieve the search results. Status code: {response.status_code}')

# Example usage
scrape_boulanger('clavier led')