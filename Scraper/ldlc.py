import requests
from bs4 import BeautifulSoup
import urllib.parse

# Fonction pour scraper le site de ldlc pour obtenir le prix d'un produit
def scrape_ldlc(query):
    # Encode la requete
    query = urllib.parse.quote_plus(query)
    #replace les espaces par des %20
    query = query.replace('+', '%20')

    # Trouve l'url du website qua,d tu fais une recherche sur le site
    #construis l'url avec la requete
    url = f'https://www.ldlc.com/recherche/{query}'
    print(url)

    # Send request to the website
    
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, allow_redirects=True)

    # Verifie que la requete fonctionne
    if response.status_code == 200:  #code 200 = OK
        # Parse le contenu de la page avec BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        #print(soup.prettify())
        
        #get every li that starts with "pdt-" in the id
        products = soup.find_all('li', id=lambda x: x and x.startswith('pdt-'))   
        firstProduct=products[0]
        #find div with class "price"
        price = firstProduct.find('div', class_='price')
        print(price.text)
        price2=price.text.replace('€', '.')
        print("print price2")
        print(price2)
        priceValue=float(price2)
        print(priceValue)
        TVA=priceValue+priceValue*0.2
        print(TVA)
        
    else:
        print(f'Failed to retrieve the search results. Status code: {response.status_code}')

# Example usage
scrape_ldlc('airpods')